# Generated by Django 3.2.12 on 2025-07-02 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bankapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='password',
            field=models.CharField(default=None, max_length=30),
        ),
    ]
