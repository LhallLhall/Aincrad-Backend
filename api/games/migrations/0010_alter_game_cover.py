# Generated by Django 4.1.3 on 2022-12-09 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0009_game_cover'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='cover',
            field=models.CharField(default='', max_length=255),
        ),
    ]
