# Generated by Django 2.2.5 on 2019-12-22 04:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vacancy', '0012_applications_email'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vacancy',
            options={'verbose_name_plural': 'Vacancy'},
        ),
        migrations.RemoveField(
            model_name='vacancy',
            name='created_at',
        ),
    ]
