# Generated by Django 3.2 on 2021-04-27 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Results',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipe_name', models.CharField(max_length=200, verbose_name='recipe name')),
                ('add_D', models.DateField(verbose_name='date added')),
                ('start_DT', models.DateTimeField(verbose_name='date & time recipe started')),
                ('test_DT', models.DateTimeField(verbose_name='date & time of test')),
                ('end_DT', models.DateTimeField(verbose_name='date & time recipe ended')),
                ('test_intervals', models.IntegerField(verbose_name='Number of times tested')),
                ('rating', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], unique=True)),
                ('notes', models.CharField(max_length=900, verbose_name='thoughts or changes')),
            ],
        ),
    ]
