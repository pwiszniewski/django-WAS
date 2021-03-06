# Generated by Django 2.2.7 on 2019-12-03 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='email',
            name='role',
            field=models.CharField(blank=True, choices=[('home', 'Home'), ('work', 'Work'), (None, 'Other')], default=None, max_length=30, null=True, verbose_name='Role'),
        ),
        migrations.AddField(
            model_name='email',
            name='user_name',
            field=models.CharField(blank=True, default=None, max_length=30, null=True, verbose_name='User Name'),
        ),
    ]
