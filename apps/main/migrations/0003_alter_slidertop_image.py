# Generated by Django 3.2 on 2021-10-02 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_slidertop_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slidertop',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='slider-top/images'),
        ),
    ]