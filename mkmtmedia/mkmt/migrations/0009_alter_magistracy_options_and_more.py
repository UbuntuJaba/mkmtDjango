# Generated by Django 4.1.3 on 2023-05-24 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mkmt', '0008_remove_magistracy_trainingperiod_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='magistracy',
            options={'ordering': ['id'], 'verbose_name': 'Магистратура ', 'verbose_name_plural': 'Магистратура'},
        ),
        migrations.AlterField(
            model_name='studyingprograms',
            name='priceDL',
            field=models.TextField(blank=True, null=True, verbose_name='Стоимость заочного обучения'),
        ),
        migrations.AlterField(
            model_name='studyingprograms',
            name='priceFT',
            field=models.TextField(blank=True, null=True, verbose_name='Стоимость очного обучения'),
        ),
        migrations.AlterField(
            model_name='studyingprograms',
            name='pricePT',
            field=models.TextField(blank=True, null=True, verbose_name='Стоимость очно-заочного обучения'),
        ),
    ]
