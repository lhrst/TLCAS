# Generated by Django 3.1.4 on 2021-02-25 15:38

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('userinfo', '0011_auto_20210225_1500'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinformation',
            name='uuid',
            field=models.CharField(default=uuid.UUID('69f35713-773c-11eb-8f7d-244bfe0424a0'), max_length=36),
        ),
    ]
