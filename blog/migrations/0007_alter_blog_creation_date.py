# Generated by Django 4.2.6 on 2024-02-11 19:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_blog_creation_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 11, 22, 0, 57, 974923), verbose_name='Дата создания'),
        ),
    ]