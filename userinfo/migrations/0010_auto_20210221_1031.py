# Generated by Django 3.1.4 on 2021-02-21 10:31

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('userinfo', '0009_auto_20201021_2115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinformation',
            name='uuid',
            field=models.CharField(default=uuid.UUID('ea5dbc03-73ec-11eb-8e93-244bfe0424a0'), max_length=36),
        ),
    ]
