# Generated by Django 3.0.5 on 2020-04-29 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('to_email', models.EmailField(default='', max_length=50)),
                ('subject', models.CharField(default='', max_length=50)),
                ('message', models.CharField(default='', max_length=300)),
            ],
        ),
    ]
