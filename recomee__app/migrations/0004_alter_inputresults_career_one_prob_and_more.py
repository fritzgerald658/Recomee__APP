# Generated by Django 4.2.12 on 2024-05-17 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recomee__app', '0003_inputresults_user_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inputresults',
            name='career_one_prob',
            field=models.IntegerField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='inputresults',
            name='career_three',
            field=models.IntegerField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='inputresults',
            name='career_two_prob',
            field=models.IntegerField(max_length=100, null=True),
        ),
    ]