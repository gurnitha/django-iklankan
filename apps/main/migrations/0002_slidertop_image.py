# Generated by Django 3.2 on 2021-10-02 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='slidertop',
            name='image',
            field=models.ImageField(blank=True, upload_to='slider-top/images'),
        ),
    ]