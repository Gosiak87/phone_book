# Generated by Django 2.0.2 on 2018-04-09 09:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phone_book_app', '0008_remove_person_group'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Groups',
        ),
    ]