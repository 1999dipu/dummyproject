# Generated by Django 3.0.5 on 2020-04-22 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lead',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('addressfield', models.CharField(max_length=100)),
                ('zipfield', models.CharField(max_length=100)),
                ('landmarksfield', models.CharField(max_length=100)),
                ('lockerfield', models.CharField(max_length=100)),
                ('query', models.CharField(max_length=100)),
            ],
        ),
    ]
