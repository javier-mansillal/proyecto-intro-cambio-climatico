# Generated by Django 3.2.9 on 2021-12-06 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Metano',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('año', models.IntegerField()),
                ('actividad', models.CharField(max_length=30)),
                ('cantidad', models.FloatField()),
            ],
        ),
    ]
