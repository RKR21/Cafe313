# Generated by Django 4.1.6 on 2023-05-23 15:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cafe', '0005_menuitems'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MenuItems',
            new_name='MenuItem',
        ),
    ]