# Generated by Django 5.0.2 on 2024-02-20 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home1', '0009_addjobs_delete_jobshow'),
    ]

    operations = [
        migrations.AddField(
            model_name='addjobs',
            name='jcompany',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='addjobs',
            name='jimage',
            field=models.ImageField(default='', upload_to='home1/images'),
        ),
    ]
