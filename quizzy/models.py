from django.db import models

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

    description = models.CharField("Вопрос", max_length=300, null=False, blank=False)
    difficulty = models.CharField("Сложность", max_length=1, choices=rang, default=rang[1][0])
    direction = models.CharField("Направление", max_length=10, choices=direct, default=direct[0][0])

    def allAnswers(self):
        return Ask.objects.filter(pk=self.id)

    def __str__(self):
        return self.description


class Ask(models.Model):
    question = models.ForeignKey('Question', on_delete=models.CASCADE)
    ask = models.CharField("Ответ", max_length=300, null=False, blank=False)
    is_correct = models.BooleanField("Верно", default=False)

    # def __str__(self):
    #     return f'Ответ на вопрос {self.question.id}'