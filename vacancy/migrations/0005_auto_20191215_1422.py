# Generated by Django 2.2.5 on 2019-12-15 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacancy', '0004_auto_20191206_0309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applications',
            name='cv',
            field=models.FileField(null=True, upload_to='Cv'),
        ),
    ]
