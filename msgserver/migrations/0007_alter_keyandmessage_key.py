# Generated by Django 3.2.8 on 2021-10-29 20:42

from django.db import migrations, models
import msgserver.models


class Migration(migrations.Migration):

    dependencies = [
        ('msgserver', '0006_alter_keyandmessage_key'),
    ]

    operations = [
        migrations.AlterField(
            model_name='keyandmessage',
            name='key',
            field=models.CharField(max_length=8, validators=[msgserver.models.valid_characters_key, msgserver.models.length_key, msgserver.models.unique_key]),
        ),
    ]
