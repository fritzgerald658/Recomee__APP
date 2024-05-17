# Generated by Django 4.2.12 on 2024-05-17 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recomee__app', '0006_rename_user_data_inputresults_user_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inputresults',
            name='user_name',
        ),
        migrations.AddField(
            model_name='inputresults',
            name='user_name',
            field=models.ManyToManyField(blank=True, null=True, to='recomee__app.username'),
        ),
    ]
