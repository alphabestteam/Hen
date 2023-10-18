# Generated by Django 4.2.6 on 2023-10-17 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('name', models.CharField(max_length=20)),
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('birth_data', models.DateField()),
                ('city', models.CharField(max_length=20)),
            ],
        ),
    ]
