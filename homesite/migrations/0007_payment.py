# Generated by Django 3.0.4 on 2020-04-10 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homesite', '0006_auto_20200410_2135'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('payment_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('amount', models.FloatField()),
                ('date', models.DateField(auto_now=True)),
            ],
        ),
    ]
