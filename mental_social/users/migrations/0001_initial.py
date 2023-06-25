# Generated by Django 4.2.2 on 2023-06-25 19:05

import datetime
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default=None, max_length=50, validators=[django.core.validators.MinLengthValidator(1)])),
                ('last_name', models.CharField(default=None, max_length=50, validators=[django.core.validators.MinLengthValidator(1)])),
                ('phone', models.CharField(default='phone', max_length=50)),
                ('birth_date', models.DateField(default=datetime.datetime.now)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], default='M', max_length=1)),
                ('person', models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='person_info', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default=None, max_length=50, validators=[django.core.validators.MinLengthValidator(1)])),
                ('last_name', models.CharField(default=None, max_length=50, validators=[django.core.validators.MinLengthValidator(1)])),
                ('certificate', models.ImageField(upload_to='certificates/')),
                ('specialty', models.CharField(choices=[('Dermatologist', 'Dermatologist'), ('Cardiologist', 'Cardiologist'), ('Pediatrician', 'Pediatrician'), ('Ophthalmologist', 'Ophthalmologist'), ('Neurologist', 'Neurologist')], default='Dermatologist', max_length=50)),
                ('office_location', models.CharField(blank=True, default='office', max_length=100, null=True)),
                ('years_of_experience', models.PositiveIntegerField(blank=True, default=1, null=True)),
                ('phone', models.CharField(default='phone', max_length=50)),
                ('birth_date', models.DateField(default=datetime.datetime.now)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], default='M', max_length=1)),
                ('person', models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='doctor', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
