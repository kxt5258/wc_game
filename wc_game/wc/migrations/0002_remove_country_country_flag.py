# Generated by Django 2.0.6 on 2018-06-07 14:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wc', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='country',
            name='country_flag',
        ),
    ]
