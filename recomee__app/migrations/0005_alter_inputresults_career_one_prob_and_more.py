# Generated by Django 4.2.12 on 2024-05-17 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recomee__app', '0004_alter_inputresults_career_one_prob_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inputresults',
            name='career_one_prob',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='inputresults',
            name='career_three',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='inputresults',
            name='career_three_prob',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='inputresults',
            name='career_two_prob',
            field=models.IntegerField(null=True),
        ),
    ]
