# Generated by Django 2.2.10 on 2020-02-29 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='firstname',
            field=models.CharField(default=0, max_length=128),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='lastname',
            field=models.CharField(default=0, max_length=128),
            preserve_default=False,
        ),
    ]
