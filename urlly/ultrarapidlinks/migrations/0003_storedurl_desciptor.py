# Generated by Django 3.0.8 on 2020-08-19 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ultrarapidlinks', '0002_auto_20200804_1801'),
    ]

    operations = [
        migrations.AddField(
            model_name='storedurl',
            name='desciptor',
            field=models.CharField(blank=True, max_length=255, verbose_name='URL Descriptor'),
        ),
    ]
