# Generated by Django 4.1.3 on 2023-05-18 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mkmt', '0002_studyingprograms_budgetplaces_studyingprograms_ege_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studyingprograms',
            name='price',
        ),
        migrations.AddField(
            model_name='studyingprograms',
            name='priceDL',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='studyingprograms',
            name='priceFT',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='studyingprograms',
            name='pricePT',
            field=models.TextField(blank=True),
        ),
    ]
