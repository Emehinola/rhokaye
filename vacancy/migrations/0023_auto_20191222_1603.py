# Generated by Django 2.2.5 on 2019-12-23 00:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vacancy', '0022_auto_20191222_0642'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='applications',
            name='email_address',
        ),
        migrations.RemoveField(
            model_name='applications',
            name='phone',
        ),
    ]