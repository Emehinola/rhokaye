# Generated by Django 2.2.5 on 2019-12-22 04:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20191221_0341'),
    ]

    operations = [
        migrations.AddField(
            model_name='staffprofile',
            name='email',
            field=models.EmailField(default=django.utils.timezone.now, max_length=254),
            preserve_default=False,
        ),
    ]
