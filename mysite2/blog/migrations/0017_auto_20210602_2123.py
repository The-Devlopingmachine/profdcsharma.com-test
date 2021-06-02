# Generated by Django 3.2.2 on 2021-06-02 15:53

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_auto_20210602_1931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='corona_help',
            name='published_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 6, 2, 15, 53, 47, 557210, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='published_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 6, 2, 15, 53, 47, 557210, tzinfo=utc), null=True),
        ),
    ]