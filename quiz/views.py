from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Question, UserQuizSession
import random

# Login Page
def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        # Check for the specific user only
        if username != "quizuser":  # Replace 'quizuser' with your specific username
            return render(request, "login.html", {"error": "Access restricted to a specific user!"})

        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect("quiz:start")  # Redirect to quiz start page
        else:
            return render(request, "login.html", {"error": "Invalid credentials. Try again!"})
    return render(request, "login.html")


# Logout View
def user_logout(request):
    logout(request)
    return redirect("quiz:login")

# Initialize session or reset
@login_required
def start_quiz(request):
    session, _ = UserQuizSession.objects.get_or_create(id=1)
    session.total_attempts = 0
    session.correct_attempts = 0
    session.incorrect_attempts = 0
    session.save()

    all_questions = list(Question.objects.all())
    if len(all_questions) < 10:
        return render(request, "index.html", {"message": "Not enough questions in the database. Add at least 10 questions."})

    request.session['quiz_questions'] = random.sample([q.id for q in all_questions], 10)
    return redirect("quiz:form_questions")

# Render the form with all 10 questions
@login_required
def form_questions(request):
    question_ids = request.session.get('quiz_questions', [])
    questions = Question.objects.filter(id__in=question_ids)
    return render(request, "form_questions.html", {"questions": questions})

# Submit the form with all answers and evaluate
@login_required
def submit_answers(request):
    if request.method == "POST":
        submitted_answers = request.POST
        question_ids = request.session.get('quiz_questions', [])
        questions = Question.objects.filter(id__in=question_ids)

        session, _ = UserQuizSession.objects.get_or_create(id=1)
        session.total_attempts = len(question_ids)

        results = []
        for question in questions:
            user_answer = submitted_answers.get(f"answer_{question.id}", "")
            is_correct = question.correct_option == user_answer
            if is_correct:
                session.correct_attempts += 1
            else:
                session.incorrect_attempts += 1
            results.append({
                "question": question.text,
                "correct_option": question.correct_option,
                "user_answer": user_answer,
                "is_correct": is_correct
            })

        session.save()
        return render(request, "result.html", {"results": results, "total": session.total_attempts})

# Show overall results
@login_required
def results(request):
    session = UserQuizSession.objects.get(id=1)
    return render(request, "result.html", {
        "total": session.total_attempts,
        "correct": session.correct_attempts,
        "incorrect": session.incorrect_attempts,
    })
