# Generated by Django 2.2.5 on 2019-10-17 11:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20190916_0247'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to=None, verbose_name=''),
            preserve_default=False,
        ),
    ]
