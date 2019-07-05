# Generated by Django 2.2.3 on 2019-07-05 01:20

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('par', models.IntegerField()),
                ('slope', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('handicap', models.CharField(max_length=200)),
                ('season_poIntegers', models.IntegerField()),
                ('rank', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('player_one_score', models.IntegerField()),
                ('player_two_score', models.IntegerField()),
                ('player_three_score', models.IntegerField()),
                ('player_four_score', models.IntegerField()),
                ('played_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tracker.Course')),
                ('player_four', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='player_four', to='tracker.Player')),
                ('player_one', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='player_one', to='tracker.Player')),
                ('player_three', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='player_three', to='tracker.Player')),
                ('player_two', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='player_two', to='tracker.Player')),
            ],
        ),
    ]
