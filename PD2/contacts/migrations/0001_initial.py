# Generated by Django 2.2.7 on 2019-12-03 22:16

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=30, verbose_name='Last Name')),
                ('date_of_birth', models.DateField(blank=True, default=None, null=True, verbose_name='Date of Birth')),
                ('pesel', models.PositiveIntegerField(blank=True, default=None, help_text='Type your PESEL number', null=True, verbose_name='PESEL')),
                ('image', models.ImageField(blank=True, default=None, null=True, upload_to='image/', verbose_name='Image')),
                ('homepage', models.URLField(blank=True, default=None, null=True, verbose_name='Homepage')),
                ('notes', models.TextField(blank=True, default=None, null=True, verbose_name='Notes')),
                ('height', models.DecimalField(blank=True, decimal_places=1, default=None, help_text='Please enter height in cm', max_digits=4, null=True, validators=[django.core.validators.MinValueValidator(100), django.core.validators.MaxValueValidator(220)], verbose_name='Height')),
                ('gender', models.CharField(blank=True, choices=[('male', 'Male'), ('female', 'Female'), (None, 'Unspecified')], default=None, max_length=30, null=True, verbose_name='Gender')),
                ('friends', models.ManyToManyField(blank=True, default=None, to='contacts.Person', verbose_name='Firends')),
            ],
            options={
                'verbose_name': 'Person',
                'verbose_name_plural': 'People',
            },
        ),
    ]