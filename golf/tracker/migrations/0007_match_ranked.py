# Generated by Django 2.2.3 on 2019-07-05 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0006_auto_20190705_0133'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='ranked',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
