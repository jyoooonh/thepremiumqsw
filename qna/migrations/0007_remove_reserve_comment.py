# Generated by Django 4.1 on 2023-03-28 12:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('qna', '0006_reserve_content_reserve_subject'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reserve',
            name='comment',
        ),
    ]
