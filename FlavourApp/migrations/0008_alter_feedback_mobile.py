# Generated by Django 3.2.1 on 2022-07-06 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FlavourApp', '0007_auto_20220706_2340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='mobile',
            field=models.IntegerField(default=None, null=True),
        ),
    ]