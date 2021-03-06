# Generated by Django 2.2.15 on 2022-01-06 12:51

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('name', models.CharField(max_length=200, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Designation',
            fields=[
                ('name', models.CharField(max_length=200, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='account',
            name='dob',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='DOB'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='account',
            name='gender',
            field=models.CharField(blank=True, choices=[('Male', 'M'), ('Female', 'F')], max_length=1, null=True, verbose_name='Gender(M/F)'),
        ),
        migrations.AddField(
            model_name='account',
            name='highest_quali',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='account',
            name='pan_no',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='account',
            name='quali_year',
            field=models.CharField(blank=True, max_length=4, null=True, verbose_name='Qualifying Year'),
        ),
        migrations.AddField(
            model_name='account',
            name='tot_experience',
            field=models.IntegerField(default=0, verbose_name='Total Experience in year'),
        ),
        migrations.AddField(
            model_name='account',
            name='Department',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='account.Department'),
        ),
        migrations.AddField(
            model_name='account',
            name='Designation',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='account.Designation'),
        ),
    ]
