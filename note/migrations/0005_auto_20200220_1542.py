# Generated by Django 3.0.1 on 2020-02-20 15:42

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0004_auto_20200218_1143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='content',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='note',
            name='created_date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2020, 2, 20, 15, 42, 56, 114419, tzinfo=utc)),
        ),
    ]
