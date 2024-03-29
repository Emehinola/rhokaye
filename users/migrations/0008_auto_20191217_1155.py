# Generated by Django 2.2.5 on 2019-12-17 19:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0007_auto_20191216_0646'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='category',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.CreateModel(
            name='StaffProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='', upload_to='posts_pics')),
                ('email', models.EmailField(default='', max_length=254)),
                ('state', models.CharField(default='', max_length=15)),
                ('nationality', models.CharField(default='', max_length=15)),
                ('address', models.CharField(default='', max_length=50)),
                ('religion', models.CharField(default='', max_length=20)),
                ('category', models.CharField(default='', max_length=30)),
                ('post', models.CharField(default='', max_length=10)),
                ('department', models.CharField(default='', max_length=30)),
                ('phone', models.CharField(default='', max_length=14)),
                ('Payment_status', models.CharField(default='', max_length=50)),
                ('date_joined', models.CharField(default='', max_length=30)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
