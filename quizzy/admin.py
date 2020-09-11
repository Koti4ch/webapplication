from django.contrib import admin
from quizzy.models import Question, Ask
# Register your models here.


class AskInline(admin.StackedInline):
    model = Ask
    can_delete = False
    verbose_name = 'Ответ'
    verbose_name_plural = 'Ответы'


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    inlines = [AskInline,]