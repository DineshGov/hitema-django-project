# Generated by Django 2.2.2 on 2019-06-07 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academy', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sport',
            name='nomSport',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]