# Generated by Django 2.1.2 on 2018-10-14 08:49

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
                ('name', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=52)),
                ('telephone', models.CharField(default='', max_length=11)),
                ('address', models.CharField(default='', max_length=100)),
                ('email', models.CharField(max_length=30)),
                ('zip_code', models.CharField(default='', max_length=6)),
                ('receive_address', models.CharField(default='', max_length=100)),
            ],
        ),
    ]
