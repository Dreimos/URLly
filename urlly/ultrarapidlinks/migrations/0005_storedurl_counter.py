# Generated by Django 3.0.8 on 2020-08-26 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ultrarapidlinks', '0004_auto_20200819_1247'),
    ]

    operations = [
        migrations.AddField(
            model_name='storedurl',
            name='counter',
            field=models.IntegerField(default=0, verbose_name='Usage counter'),
        ),
    ]
