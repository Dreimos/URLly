# Generated by Django 3.0.8 on 2020-08-19 09:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ultrarapidlinks', '0003_storedurl_desciptor'),
    ]

    operations = [
        migrations.RenameField(
            model_name='storedurl',
            old_name='desciptor',
            new_name='descriptor',
        ),
    ]