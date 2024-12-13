# **Django Quiz Application**

This project is a **multiple-choice quiz application** built using Django. It allows a single user to log in, answer 10 randomly selected questions from a pool of questions, and view the results. The application includes user authentication, session management, and the ability to log out at any stage.

---

## **Features**

1. **User Authentication**:  
   - A single user with predefined credentials can log in to access the quiz.  

2. **Randomized Questions**:  
   - 10 questions are randomly selected from a pool of available questions.  

3. **Quiz Form**:  
   - All 10 questions are displayed in a single form.  
   - Users can select answers and submit them at once.  

4. **Answer Evaluation**:  
   - The application evaluates the submitted answers and shows:  
     - Correct answers  
     - Incorrect answers  
     - Total attempts  

5. **Logout Functionality**:  
   - A **logout button** is available at the top-right corner on every page.  
   - Clicking the button logs the user out and redirects them to the login page.  

6. **Session Management**:  
   - Upon logout, the session is cleared, and the quiz starts afresh after re-login.

---

## **Technologies Used**

- **Django** (Web Framework)
- **SQLite** (Default Database)
- **HTML/CSS** (Frontend)

---

## **Setup Instructions**

Follow these steps to set up and run the project locally:

### **1. Clone the Repository**

```bash
git clone https://github.com/RajdeepDas43/QuizAppDjango.git
cd quiz_app
```

---

### **2. Create a Virtual Environment**

```bash
python -m venv venv
source venv/bin/activate       # On Linux/Mac
venv\Scripts\activate          # On Windows
```

---

### **3. Install Dependencies**

```bash
pip install django
```

---

### **4. Run Migrations**

```bash
python manage.py makemigrations
python manage.py migrate
```

---

### **5. Create a Superuser**

To access the admin panel:

```bash
python manage.py createsuperuser
```
- Set a **username** and **password** (e.g., `quizuser`).

---

### **6. Add Questions**

1. Start the server:
   ```bash
   python manage.py runserver
   ```
2. Go to the **admin panel**:
   ```
   http://127.0.0.1:8000/admin/
   ```
3. Log in with your superuser credentials.
4. Add at least **20 questions** under the **Question** model:
   - **Text**: Question text  
   - **Option A, B, C, D**: Multiple-choice options  
   - **Correct Option**: The correct answer (e.g., "A").

---

### **7. Run the Application**

Start the server:
```bash
python manage.py runserver
```
Access the application in your browser:
```
http://127.0.0.1:8000/
```

---

## **How to Use the Application**

### **1. Login**
- On visiting the root URL (`/`), the login page will appear.
- Log in using the predefined credentials:
  - **Username**: `quizuser`  
  - **Password**: (Set during superuser creation).

---

### **2. Start the Quiz**
- Upon login, you will be redirected to the **quiz start page**.
- Click **Start Quiz** to begin.

---

### **3. Answer Questions**
- A form with **10 random questions** will appear.
- Select the correct answers for each question using the radio buttons.
- Submit the form.

---

### **4. View Results**
- After submitting, the results page will display:
  - Question text
  - Your selected answer
  - Correct answer
  - Whether your answer was correct or incorrect
- You will also see the total correct and incorrect answers.

---

### **5. Logout**
- A **Logout** button is available at the top-right corner of every page.
- Clicking **Logout** will log you out and redirect you to the login page.

---

## **URL Endpoints**

| **URL**                    | **Method** | **Description**                                |
|----------------------------|------------|-----------------------------------------------|
| `/`                        | `GET`      | Displays the login page.                      |
| `/quiz/start/`             | `GET`      | Starts the quiz and selects 10 random questions. |
| `/quiz/form/`              | `GET`      | Displays the form with all 10 questions.      |
| `/quiz/submit/`            | `POST`     | Submits the answers and evaluates them.       |
| `/quiz/results/`           | `GET`      | Displays the quiz results.                    |
| `/quiz/logout/`            | `POST`     | Logs the user out and redirects to the login page. |
| `/admin/`                  | `GET`      | Admin panel for managing users and questions. |

---

## **Example Workflow**

1. Visit `http://127.0.0.1:8000/`.
2. Log in using:
   - Username: `quizuser`
   - Password: algoquiz432.
3. Start the quiz and answer the questions.
4. Submit the form and view your results.
5. Log out using the **Logout** button.

---

## **Screenshots**

### Login Page
<img width="376" alt="image" src="https://github.com/user-attachments/assets/61cba7b2-d7df-4a08-bc51-b614d0302190" />



### Quiz Form
![Quiz Form](screenshot_form.png)

### Results Page
![Results Page](screenshot_results.png)

---

## **Future Improvements**
- Allow multiple users to take the quiz.
- Add a feature to create or edit questions from the frontend.
- Implement user-specific quiz history.

---

## **License**

This project is licensed under the MIT License.

---

Let me know if you need further modifications or if you'd like help adding screenshots! 🚀
