# Generated by Django 3.2.2 on 2021-07-03 04:46

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0020_auto_20210626_2007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='corona_help',
            name='published_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 7, 3, 4, 46, 33, 929298, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='published_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 7, 3, 4, 46, 33, 929298, tzinfo=utc), null=True),
        ),
    ]