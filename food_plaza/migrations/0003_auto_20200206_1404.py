# Generated by Django 3.0.2 on 2020-02-06 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food_plaza', '0002_recipe_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe_table',
            name='desc',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='recipe_table',
            name='ingredient',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='recipe_table',
            name='pom',
            field=models.CharField(max_length=2000),
        ),
    ]