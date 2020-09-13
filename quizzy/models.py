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

    description = models.CharField("Вопрос", max_length=300, null=False, blank=False, unique=True)
    difficulty = models.CharField("Сложность", max_length=1, choices=rang, default=rang[1][0])
    direction = models.CharField("Направление", max_length=10, choices=direct, default=direct[0][0])

    def __str__(self):
        return f'{self.description[:10]}...'

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'



class Ask(models.Model):
    question = models.ForeignKey('question', on_delete=models.CASCADE)
    ask = models.CharField("Ответ", max_length=300, null=False, blank=False)
    is_correct = models.BooleanField("Верно", default=False)

    def __str__(self):
        return f'{self.question_id}'