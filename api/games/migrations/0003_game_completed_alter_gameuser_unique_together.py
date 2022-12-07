# Generated by Django 4.1.3 on 2022-12-05 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0002_game_gameuser_customuser_games'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='completed',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterUniqueTogether(
            name='gameuser',
            unique_together={('game', 'user')},
        ),
    ]
