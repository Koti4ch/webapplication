from django.contrib import admin
from quizzy.models import Question, Ask
# Register your models here.


class AskInline(admin.StackedInline):
    model = Ask
    fields = (('ask', 'is_correct'), )
    can_delete = True
    extra = 1
    min_num = None
    verbose_name = 'Ответ'
    verbose_name_plural = 'Ответы'


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    inlines = [AskInline,]
    list_display = ('__str__', 'difficulty', 'direction', 'allanswers')

    def allanswers(self, obj):
        return Ask.objects.filter(question_id=obj.id).count()
    allanswers.short_description = 'Всего ответов'