# Generated by Django 4.2.6 on 2023-10-25 08:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_unread_messages'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='unread_messages',
        ),
    ]