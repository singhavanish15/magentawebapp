# Generated by Django 4.1.1 on 2022-09-22 11:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_rename_contacts_person'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='person',
            new_name='contact',
        ),
    ]
