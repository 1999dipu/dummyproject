# Generated by Django 3.0.5 on 2020-04-29 06:58

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lockers', '0004_auto_20200429_1217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='availability',
            name='non_del_days',
            field=models.CharField(default='0000000', max_length=7, validators=[django.core.validators.RegexValidator('^\\d{1,10}$', message='Letters not permissible')], verbose_name='Non delivery days'),
        ),
        migrations.AlterField(
            model_name='onboard',
            name='country',
            field=models.CharField(max_length=100, validators=[django.core.validators.RegexValidator('^[a-zA-Z ]+$', message='Numbers not permissible')]),
        ),
        migrations.AlterField(
            model_name='onboard',
            name='name',
            field=models.CharField(max_length=250, validators=[django.core.validators.RegexValidator('^[a-zA-Z ]+$', message='Numbers not permissible')]),
        ),
        migrations.AlterField(
            model_name='onboard',
            name='zipcode',
            field=models.CharField(max_length=6, validators=[django.core.validators.RegexValidator('^\\d{1,10}$', message='Only 6 digit zipcodes are permissible')]),
        ),
    ]
