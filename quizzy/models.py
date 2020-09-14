from django.db import models
from django.db.models import Avg, Count, Min, Sum
# Create your models here.


class Question(models.Model):
    rang = (
        ('e', "Простой"),
        ('n', "Нормальный"),
        ('h', "Сложный")
    )
    direct = (
        ("base", "Общие"),
        ("electro", "Электробезопастность"),
        ("medic", "Медицина"),
        ("znak", "Знаки"),
    )

    nums = (
        (str(_), str(_)) for _ in range(1, 10)
    )

    description = models.CharField("Вопрос", max_length=300, null=False, blank=False, unique=True)
    difficulty = models.CharField("Сложность", max_length=1, choices=rang, default=rang[1][0])
    direction = models.CharField("Направление", max_length=10, choices=direct, default=direct[0][0])
    max_correct_answers = models.CharField("Количество правильных ответов на вопрос", max_length=1, choices=nums, default=rang[1][0])

    def __str__(self):
        return f'{self.description[:15]}...'

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'


class Ask(models.Model):
    question = models.ForeignKey('question', on_delete=models.CASCADE)
    ask = models.CharField("Ответ", max_length=300, null=False, blank=False)
    is_correct = models.BooleanField("Верно", default=False)

#   TODO: think how create show 1,2,3,4,5,6, etc
    def __str__(self):
        return f'#{self.id}'