# Generated by Django 3.2.2 on 2021-06-02 14:01

import ckeditor.fields
import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_auto_20210522_0111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='corona_help',
            name='discreption',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='corona_help',
            name='published_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 6, 2, 14, 1, 7, 269984, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='published_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 6, 2, 14, 1, 7, 268962, tzinfo=utc), null=True),
        ),
    ]
