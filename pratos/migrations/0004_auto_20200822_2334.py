# Generated by Django 3.1 on 2020-08-23 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pratos', '0003_auto_20200822_2333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='price',
            field=models.CharField(max_length=50),
        ),
    ]
