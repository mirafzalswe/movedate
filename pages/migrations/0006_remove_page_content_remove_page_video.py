# Generated by Django 4.2 on 2024-03-15 19:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_alter_page_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='page',
            name='content',
        ),
        migrations.RemoveField(
            model_name='page',
            name='video',
        ),
    ]
