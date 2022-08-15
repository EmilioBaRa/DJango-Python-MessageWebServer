# Generated by Django 3.2.8 on 2021-10-27 23:13

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('msgserver', '0002_alter_keyandmessage_key'),
    ]

    operations = [
        migrations.AlterField(
            model_name='keyandmessage',
            name='key',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(10000000), django.core.validators.MaxValueValidator(99999999)]),
        ),
    ]