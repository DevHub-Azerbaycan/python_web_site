# Generated by Django 2.2.7 on 2020-04-12 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200412_1112'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='viewed',
        ),
        migrations.AddField(
            model_name='post',
            name='viewed',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
