# Generated by Django 3.0.7 on 2023-09-21 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20230921_0133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='treinamento',
            name='codigo_curso',
            field=models.CharField(max_length=5, unique=True),
        ),
    ]
