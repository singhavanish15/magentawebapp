# Generated by Django 4.1.1 on 2022-10-13 14:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_alter_gallery1_typename_bgpic_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery_subitem',
            name='gallery1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gallery1', to='home.gallery1'),
        ),
    ]