# Generated by Django 3.0.7 on 2020-11-27 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='userid',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
