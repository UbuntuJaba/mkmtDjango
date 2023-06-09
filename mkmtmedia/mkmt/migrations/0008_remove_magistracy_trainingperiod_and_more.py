# Generated by Django 4.1.3 on 2023-05-23 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mkmt', '0007_alter_magistracy_pricedl_alter_magistracy_priceft_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='magistracy',
            name='trainingPeriod',
        ),
        migrations.AddField(
            model_name='magistracy',
            name='trainingPeriodDL',
            field=models.TextField(blank=True, null=True, verbose_name='Срок заочного обучения'),
        ),
        migrations.AddField(
            model_name='magistracy',
            name='trainingPeriodFT',
            field=models.TextField(blank=True, null=True, verbose_name='Срок очного обучения'),
        ),
        migrations.AddField(
            model_name='magistracy',
            name='trainingPeriodPT',
            field=models.TextField(blank=True, null=True, verbose_name='Срок очно-заочного обучения'),
        ),
    ]
