# Generated by Django 2.2.7 on 2019-12-16 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Jishusei',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('introduction', models.TextField()),
                ('edu_background', models.TextField()),
                ('carrer_background', models.TextField()),
                ('profile_pic', models.ImageField(upload_to='profile_pic/')),
            ],
        ),
    ]