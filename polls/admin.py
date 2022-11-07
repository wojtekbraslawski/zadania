from django.contrib import admin
from . models import Question, Answer, Choice

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    date_hierarchy = 'pub_date'
    ordering=['pub_date','type','question_text']
    list_display = ('question_text', 'pub_date', 'type')

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    ordering = ['question','user_answer']
    list_display = ('user_answer', 'question')
    raw_id_fields = ('question',)

@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    ordering = ['votes',"question","choice_text"]
    list_display = ('choice_text', 'question','votes')
    raw_id_fields = ('question',)
# Register your models here.
