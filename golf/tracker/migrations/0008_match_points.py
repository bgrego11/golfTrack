# Generated by Django 2.2.3 on 2019-07-05 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0007_match_ranked'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='points',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
