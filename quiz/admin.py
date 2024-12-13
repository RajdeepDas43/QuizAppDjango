from django.contrib import admin
from .models import Question

# Register the Question model
@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ("text", "correct_option")  # Fields to display in the admin list
