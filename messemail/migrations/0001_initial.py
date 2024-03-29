# Generated by Django 4.2.6 on 2023-10-30 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='имя')),
                ('email', models.EmailField(max_length=150, unique=True, verbose_name='почта')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='комментарий')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'клиент',
                'verbose_name_plural': 'клиенты',
            },
        ),
    ]
