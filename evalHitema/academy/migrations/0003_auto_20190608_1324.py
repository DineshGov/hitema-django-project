# Generated by Django 2.2.2 on 2019-06-08 11:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('academy', '0002_auto_20190607_2319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sport',
            name='nomSport',
            field=models.CharField(error_messages={'unique': 'Un sport du même nom existe déjà!'}, max_length=100, unique=True),
        ),
        migrations.CreateModel(
            name='Equipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomEquipe', models.CharField(error_messages={'max_length': 'Veuillez choisir un nom plus court.', 'unique': 'Une équipe du même nom existe déjà!'}, max_length=100, unique=True)),
                ('sport', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='academy.Sport')),
            ],
            options={
                'verbose_name': 'equipe',
            },
        ),
    ]