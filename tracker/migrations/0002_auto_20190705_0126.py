# Generated by Django 2.2.3 on 2019-07-05 01:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='player',
            old_name='season_poIntegers',
            new_name='season_points',
        ),
        migrations.RemoveField(
            model_name='match',
            name='title',
        ),
    ]