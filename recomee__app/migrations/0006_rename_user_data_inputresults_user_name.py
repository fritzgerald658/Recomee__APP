# Generated by Django 4.2.12 on 2024-05-17 11:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recomee__app', '0005_alter_inputresults_career_one_prob_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='inputresults',
            old_name='user_data',
            new_name='user_name',
        ),
    ]