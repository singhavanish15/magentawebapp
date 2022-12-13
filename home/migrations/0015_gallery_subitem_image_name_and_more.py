# Generated by Django 4.1.1 on 2022-11-10 07:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_alter_gallery_subitem_gallery1'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery_subitem',
            name='image_name',
            field=models.CharField(default=False, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='gallery_subitem',
            name='gallery1',
            field=models.ForeignKey(default=False, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.gallery1'),
        ),
    ]