# Generated by Django 4.1.6 on 2023-05-09 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cafe', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dailyspecial',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
