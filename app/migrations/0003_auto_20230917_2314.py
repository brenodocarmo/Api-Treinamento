# Generated by Django 3.0.7 on 2023-09-18 02:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20230917_2236'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Disciplina',
            new_name='Treinamento',
        ),
        migrations.RenameField(
            model_name='treinamento',
            old_name='codigo_disciplina',
            new_name='codigo_curso',
        ),
    ]