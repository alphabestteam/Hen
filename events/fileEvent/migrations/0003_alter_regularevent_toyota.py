# Generated by Django 4.2.6 on 2023-10-24 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fileEvent', '0002_alter_regularevent_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='regularevent',
            name='toyota',
            field=models.BooleanField(default=True),
        ),
    ]
