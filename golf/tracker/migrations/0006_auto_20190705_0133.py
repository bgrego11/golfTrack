# Generated by Django 2.2.3 on 2019-07-05 01:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0005_auto_20190705_0131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='slope',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='match',
            name='player_four',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='player_four', to='tracker.Player'),
        ),
        migrations.AlterField(
            model_name='match',
            name='player_four_score',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='match',
            name='player_three',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='player_three', to='tracker.Player'),
        ),
        migrations.AlterField(
            model_name='match',
            name='player_three_score',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
