# Generated by Django 2.0.2 on 2018-03-02 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phone_book_app', '0006_auto_20180301_1756'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='number_flat',
            field=models.CharField(max_length=65, null=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='number_house',
            field=models.CharField(max_length=65, null=True),
        ),
        migrations.AlterField(
            model_name='email',
            name='address_email',
            field=models.EmailField(max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='phone',
            name='number_phone',
            field=models.CharField(max_length=65, null=True),
        ),
    ]