# Generated by Django 2.2.15 on 2022-01-07 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_auto_20220107_1619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='dt_ob',
            field=models.DateField(blank=True, null=True, verbose_name='date of birth'),
        ),
    ]
