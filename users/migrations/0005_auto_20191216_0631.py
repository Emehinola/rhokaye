# Generated by Django 2.2.5 on 2019-12-16 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20191215_1422'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='Class',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='profile',
            name='department',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='profile',
            name='occupation',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='profile',
            name='parent_name',
            field=models.ImageField(default='', upload_to=''),
        ),
        migrations.AddField(
            model_name='profile',
            name='parent_number',
            field=models.CharField(default='', max_length=14),
        ),
        migrations.AddField(
            model_name='profile',
            name='post',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='profile',
            name='religion',
            field=models.CharField(default='', max_length=20),
        ),
    ]
