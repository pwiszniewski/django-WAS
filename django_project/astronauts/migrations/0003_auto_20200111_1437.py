# Generated by Django 2.2.9 on 2020-01-11 13:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('astronauts', '0002_auto_20200110_1437'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Person',
            new_name='Astronaut',
        ),
    ]
