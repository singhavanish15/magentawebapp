# Generated by Django 4.1.1 on 2022-09-22 12:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_rename_person_contact'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='contact',
            new_name='person',
        ),
    ]
