# Generated by Django 4.1.3 on 2023-05-23 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mkmt', '0004_alter_studyingprograms_budgetplaces_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='magistracy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Программа обучения')),
                ('formOfEdu', models.TextField(blank=True, verbose_name='Форма обучения')),
                ('profile', models.TextField(blank=True, verbose_name='Профиль обучения')),
                ('priceFT', models.TextField(blank=True, verbose_name='Стоимость очного обучения')),
                ('pricePT', models.TextField(blank=True, verbose_name='Стоимость очно-заочного обучения')),
                ('priceDL', models.TextField(blank=True, verbose_name='Стоимость заочного обучения')),
            ],
            options={
                'verbose_name': 'Магистратура ',
                'verbose_name_plural': 'Магистратура',
                'ordering': ['title'],
            },
        ),
        migrations.AlterModelOptions(
            name='studyingprograms',
            options={'ordering': ['title'], 'verbose_name': 'Бакалавриат', 'verbose_name_plural': 'Бакалавриат'},
        ),
        migrations.AlterField(
            model_name='studyingprograms',
            name='budgetPlaces',
            field=models.IntegerField(blank=True, verbose_name='Бюджетные места'),
        ),
        migrations.AlterField(
            model_name='studyingprograms',
            name='ege',
            field=models.TextField(blank=True, verbose_name='ЕГЭ'),
        ),
        migrations.AlterField(
            model_name='studyingprograms',
            name='formOfEdu',
            field=models.TextField(blank=True, verbose_name='Форма обучения'),
        ),
        migrations.AlterField(
            model_name='studyingprograms',
            name='greenWave',
            field=models.IntegerField(blank=True, verbose_name='Зеленая волна'),
        ),
        migrations.AlterField(
            model_name='studyingprograms',
            name='passingScore',
            field=models.IntegerField(blank=True, verbose_name='Проходной балл'),
        ),
        migrations.AlterField(
            model_name='studyingprograms',
            name='priceDL',
            field=models.TextField(blank=True, verbose_name='Стоимость заочного обучения'),
        ),
        migrations.AlterField(
            model_name='studyingprograms',
            name='priceFT',
            field=models.TextField(blank=True, verbose_name='Стоимость очного обучения'),
        ),
        migrations.AlterField(
            model_name='studyingprograms',
            name='pricePT',
            field=models.TextField(blank=True, verbose_name='Стоимость очно-заочного обучения'),
        ),
        migrations.AlterField(
            model_name='studyingprograms',
            name='profile',
            field=models.TextField(blank=True, verbose_name='Профиль обучения'),
        ),
        migrations.AlterField(
            model_name='studyingprograms',
            name='spo',
            field=models.TextField(blank=True, verbose_name='СПО'),
        ),
        migrations.AlterField(
            model_name='studyingprograms',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Программа обучения'),
        ),
    ]