# Generated by Django 2.2.2 on 2021-06-08 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=11, verbose_name='用户名')),
                ('desc', models.CharField(max_length=100, verbose_name='个人描述')),
            ],
        ),
    ]
