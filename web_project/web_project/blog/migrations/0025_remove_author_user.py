# Generated by Django 4.2.3 on 2023-08-11 12:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0024_author_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='user',
        ),
    ]