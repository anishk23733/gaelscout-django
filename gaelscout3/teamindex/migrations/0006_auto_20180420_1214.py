# Generated by Django 2.0.4 on 2018-04-20 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teamindex', '0005_auto_20180418_1305'),
    ]

    operations = [
        migrations.AddField(
            model_name='matches',
            name='day',
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='matches',
            name='field',
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='matches',
            name='number',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='matches',
            name='phase',
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='matches',
            name='time',
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
    ]