from django.db import models

# Create your models here.
class studyingPrograms(models.Model):
    title = models.CharField(max_length = 255, verbose_name='Программа обучения')
    formOfEdu = models.TextField(blank = True, verbose_name='Форма обучения')
    budgetPlaces = models.IntegerField(blank = True, verbose_name='Бюджетные места')
    greenWave = models.IntegerField(blank = True, null = True, verbose_name='Зеленая волна')
    passingScore = models.IntegerField(blank = True, verbose_name='Проходной балл')
    profile = models.TextField(blank = True, verbose_name='Профиль обучения')
    ege = models.TextField(blank = True, verbose_name='ЕГЭ')
    spo = models.TextField(blank = True, verbose_name='СПО')
    priceFT = models.TextField(blank = True, null = True, verbose_name='Стоимость очного обучения')
    pricePT = models.TextField(blank = True, null = True, verbose_name='Стоимость очно-заочного обучения')
    priceDL = models.TextField(blank = True, null = True, verbose_name='Стоимость заочного обучения')

    class Meta:
        verbose_name = 'Бакалавриат'
        verbose_name_plural = 'Бакалавриат'
        ordering = ['title']

    def __str__(self):
        return self.title

class magistracy(models.Model):
    title = models.CharField(max_length = 255, verbose_name='Программа обучения')
    formOfEdu = models.TextField(blank = True, verbose_name='Форма обучения')
    profile = models.TextField(blank = True, verbose_name='Профиль обучения')
    priceFT = models.TextField(blank = True, null = True, verbose_name='Стоимость очного обучения')
    pricePT = models.TextField(blank = True, null = True, verbose_name='Стоимость очно-заочного обучения')
    priceDL = models.TextField(blank = True, null = True, verbose_name='Стоимость заочного обучения')
    trainingPeriodFT = models.TextField(blank = True, null = True, verbose_name='Срок очного обучения')
    trainingPeriodPT = models.TextField(blank = True, null = True, verbose_name='Срок очно-заочного обучения')
    trainingPeriodDL = models.TextField(blank = True, null = True, verbose_name='Срок заочного обучения')

    class Meta:
        verbose_name = 'Магистратура '
        verbose_name_plural = 'Магистратура'
        ordering = ['id']

    def __str__(self):
        return self.title