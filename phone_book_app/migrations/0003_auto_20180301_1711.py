# Generated by Django 2.0.2 on 2018-03-01 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phone_book_app', '0002_auto_20180301_1511'),
    ]

    operations = [
        migrations.RenameField(
            model_name='email',
            old_name='address_email',
            new_name='type_email',
        ),
        migrations.AddField(
            model_name='email',
            name='adress_email',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='phone',
            name='type_phone',
            field=models.IntegerField(choices=[(0, 'domowy'), (1, 'służbowy'), (2, 'komórkowy')], default=2),
        ),
        migrations.AlterField(
            model_name='phone',
            name='number_phone',
            field=models.IntegerField(null=True),
        ),
    ]
