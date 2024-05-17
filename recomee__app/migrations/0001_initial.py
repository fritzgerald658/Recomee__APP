# Generated by Django 4.2.12 on 2024-05-17 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InputResults',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_course', models.CharField(max_length=100, null=True)),
                ('user_industry', models.CharField(max_length=100, null=True)),
                ('user_skills', models.CharField(max_length=100, null=True)),
                ('user_interest', models.CharField(max_length=100, null=True)),
                ('career_one', models.CharField(max_length=100, null=True)),
                ('career_two', models.CharField(max_length=100, null=True)),
                ('career_three', models.CharField(max_length=100, null=True)),
                ('career_one_prob', models.CharField(max_length=100, null=True)),
                ('career_two_prob', models.CharField(max_length=100, null=True)),
                ('career_three_prob', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]