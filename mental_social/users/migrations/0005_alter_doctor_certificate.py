# Generated by Django 4.2.2 on 2023-06-27 01:54

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0004_doctor_user_type_person_user_type"),
    ]

    operations = [
        migrations.AlterField(
            model_name="doctor",
            name="certificate",
            field=models.ImageField(null=True, upload_to="certificates/"),
        ),
    ]