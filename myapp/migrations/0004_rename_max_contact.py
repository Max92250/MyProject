# Generated by Django 4.0.1 on 2022-02-23 17:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_rename_services_max'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='max',
            new_name='Contact',
        ),
    ]
