# Generated by Django 5.0 on 2023-12-14 07:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=25, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=20)),
                ('borrow_books', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_borrow_books', to='books.borrowbook')),
                ('sell_books', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_sell_books', to='books.sellbook')),
            ],
        ),
    ]