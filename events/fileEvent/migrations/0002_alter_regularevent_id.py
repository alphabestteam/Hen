# Generated by Django 4.2.6 on 2023-10-24 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fileEvent', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='regularevent',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
