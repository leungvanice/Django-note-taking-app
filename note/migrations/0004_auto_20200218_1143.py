# Generated by Django 3.0.1 on 2020-02-18 11:43

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0003_auto_20200218_1140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='created_date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2020, 2, 18, 11, 43, 49, 532753, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='note',
            name='modified_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
