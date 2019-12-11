# Generated by Django 2.2.7 on 2019-12-11 04:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='companyname',
        ),
        migrations.RemoveField(
            model_name='company',
            name='title',
        ),
        migrations.RemoveField(
            model_name='company',
            name='url',
        ),
        migrations.AddField(
            model_name='company',
            name='companyid',
            field=models.ForeignKey(default=999, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='company',
            name='location',
            field=models.CharField(default=999, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='company',
            name='name',
            field=models.CharField(default=999, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='company',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
