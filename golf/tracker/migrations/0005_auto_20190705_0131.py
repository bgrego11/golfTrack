# Generated by Django 2.2.3 on 2019-07-05 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0004_auto_20190705_0130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='handicap',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
