from django.contrib import admin
from django.forms.models import BaseInlineFormSet
from django.forms.forms import ValidationError
from django.db.models import Avg, Count, Min, Sum
from quizzy.models import Question, Ask
# Register your models here.

class OnlyOneValidate(BaseInlineFormSet):
    '''
    Валидируем на кол-во верных ответов
    '''
    def clean(self):
        checkbox = 0
        for form in self.forms:
            max_correct_answers = self.instance.max_correct_answers
            try:
                if form.cleaned_data.get('is_correct') == True:
                    checkbox += 1
            except AttributeError:
                print('AttributeError')
                pass
        print(checkbox)
        if checkbox != int(max_correct_answers):
            raise ValidationError(f'Для этого вопроса должно быть выбрано {max_correct_answers} правильных ответов!')


class AskInline(admin.StackedInline):
    model = Ask
    fields = (('ask', 'is_correct'), )
    formset = OnlyOneValidate
    can_delete = True
    extra = 1
    min_num = None
    verbose_name = 'ответ'
    verbose_name_plural = 'ответы'


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    inlines = [AskInline,]
    list_display = ('__str__', 'difficulty', 'direction', 'correctAnswers', 'allAnswers')

    def correctAnswers(self, obj):
        return obj.max_correct_answers
    correctAnswers.short_description = 'Верных ответов'
    correctAnswers.empty_value_display = '-'

    def allAnswers(self, obj):
        return Ask.objects.filter(question_id=obj.id).count()
    allAnswers.short_description = 'Всего ответов'

################################## TEST             #######################
@admin.register(Ask)
class AskAdmin(admin.ModelAdmin):
    list_display = ('aaaaaaa',)
    counter = 0

    def aaaaaaa(self, obj):
        self.counter += 1
        print(self.counter)
        return f'#{self.counter}'
