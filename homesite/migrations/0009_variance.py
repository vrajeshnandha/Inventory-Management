# Generated by Django 3.0.4 on 2020-04-12 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homesite', '0008_auto_20200412_1241'),
    ]

    operations = [
        migrations.CreateModel(
            name='Variance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('name', models.CharField(max_length=200)),
                ('variance', models.FloatField()),
                ('fabric_name', models.CharField(max_length=100)),
            ],
        ),
    ]
