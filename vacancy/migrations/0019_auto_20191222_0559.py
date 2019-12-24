# Generated by Django 2.2.5 on 2019-12-22 13:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('vacancy', '0018_auto_20191221_2232'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='applications',
            name='email',
        ),
        migrations.AddField(
            model_name='applications',
            name='email_address',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='applications',
            name='location',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='applications',
            name='phone',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='applications',
            name='qualifications',
            field=models.CharField(max_length=50),
        ),
    ]