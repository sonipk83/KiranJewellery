# Generated by Django 2.2b1 on 2019-03-14 11:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_postimage'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PostImage',
        ),
    ]