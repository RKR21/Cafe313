# Generated by Django 4.1.6 on 2023-05-09 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cafe', '0003_alter_dailyspecial_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dailyspecial',
            name='date',
            field=models.DateTimeField(),
        ),
    ]