# Generated by Django 3.1.1 on 2020-09-08 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20200908_0940'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='date',
        ),
        migrations.AddField(
            model_name='post',
            name='date_time',
            field=models.DateTimeField(),
            preserve_default=False,
        ),
    ]