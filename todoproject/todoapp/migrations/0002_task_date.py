# Generated by Django 4.0.6 on 2022-08-07 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='1994-03-06'),
            preserve_default=False,
        ),
    ]
