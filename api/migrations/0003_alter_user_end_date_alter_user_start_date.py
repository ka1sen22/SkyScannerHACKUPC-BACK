# Generated by Django 5.2 on 2025-05-03 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_suggesteddestination'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='start_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
