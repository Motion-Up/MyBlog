# Generated by Django 3.1.1 on 2020-09-08 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20200908_0951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_time',
            field=models.DateField(blank=True, null=True),
        ),
    ]
