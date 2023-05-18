from django.db import models

# Create your models here.
class studyingPrograms(models.Model):
    title = models.CharField(max_length = 255, verbose_name='Программа обучения')
    formOfEdu = models.TextField(blank = True, verbose_name='Форма обучения')
    budgetPlaces = models.IntegerField(blank = True, verbose_name='Бюджетные места')
    greenWave = models.IntegerField(blank = True, verbose_name='Зеленая волна')
    passingScore = models.IntegerField(blank = True, verbose_name='Проходной балл')
    profile = models.TextField(blank = True, verbose_name='Профиль обучения')
    ege = models.TextField(blank = True, verbose_name='ЕГЭ')
    spo = models.TextField(blank = True, verbose_name='СПО')
    priceFT = models.TextField(blank = True, verbose_name='Стоимость очного обучения')
    pricePT = models.TextField(blank = True, verbose_name='Стоимость очно-заочного обучения')
    priceDL = models.TextField(blank = True, verbose_name='Стоимость заочного обучения')

    class Meta:
        verbose_name = 'Программы обучения'
        verbose_name_plural = 'Программы обучения'
        ordering = ['title']

    def __str__(self):
        return self.title