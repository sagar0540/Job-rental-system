# Generated by Django 5.0.2 on 2024-02-21 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home1', '0011_alter_addjobs_jimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='save_form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.IntegerField()),
                ('state', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('zipcode', models.CharField(max_length=100)),
                ('Qualification', models.CharField(max_length=100)),
                ('Experience', models.CharField(max_length=100)),
            ],
        ),
    ]
