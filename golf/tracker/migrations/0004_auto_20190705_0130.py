# Generated by Django 2.2.3 on 2019-07-05 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0003_auto_20190705_0129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='handicap',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
