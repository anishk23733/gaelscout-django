# Generated by Django 2.0.4 on 2018-04-20 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teamindex', '0006_auto_20180420_1214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matches',
            name='number',
            field=models.CharField(max_length=10),
        ),
    ]
