# Generated by Django 2.0.5 on 2020-04-14 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HousingHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('postcode', models.CharField(default='', max_length=10)),
                ('addressLine1', models.CharField(default='', max_length=35)),
                ('addressLine2', models.CharField(default='', max_length=35)),
                ('city', models.CharField(default='', max_length=35)),
                ('county', models.CharField(default='', max_length=35)),
                ('country', models.CharField(default='', max_length=35)),
                ('movingDate', models.DateTimeField()),
            ],
        ),
    ]
