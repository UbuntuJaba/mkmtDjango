# Generated by Django 4.1.3 on 2023-05-23 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mkmt', '0005_magistracy_alter_studyingprograms_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='magistracy',
            name='trainingPeriod',
            field=models.TextField(blank=True, verbose_name='Срок обучения'),
        ),
    ]
