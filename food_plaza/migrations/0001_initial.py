# Generated by Django 2.2.2 on 2020-02-03 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user_reg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=14)),
                ('address', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
    ]
