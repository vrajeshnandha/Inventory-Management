# Generated by Django 3.0.4 on 2020-04-07 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homesite', '0003_stockentry'),
    ]

    operations = [
        migrations.AddField(
            model_name='stockentry',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
