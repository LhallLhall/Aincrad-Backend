# Generated by Django 4.1.3 on 2022-12-09 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0008_gameuser_completed_gameuser_created_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='cover',
            field=models.CharField(default='https://via.placeholder.com/286x381/603d60/FFFFFF?text=', max_length=255),
        ),
    ]
