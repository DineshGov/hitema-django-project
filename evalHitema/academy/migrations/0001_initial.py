# Generated by Django 2.2.2 on 2019-06-07 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomSport', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'sport',
            },
        ),
    ]