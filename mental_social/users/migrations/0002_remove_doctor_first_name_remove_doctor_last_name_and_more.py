# Generated by Django 4.2.2 on 2023-06-25 19:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='person',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='person',
            name='last_name',
        ),
    ]