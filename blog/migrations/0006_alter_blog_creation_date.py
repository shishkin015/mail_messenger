# Generated by Django 4.2.6 on 2024-02-11 18:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_blog_creation_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 11, 21, 59, 47, 389752), verbose_name='Дата создания'),
        ),
    ]
