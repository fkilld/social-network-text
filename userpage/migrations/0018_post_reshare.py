# Generated by Django 3.0 on 2020-04-29 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userpage', '0017_remove_like_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='reshare',
            field=models.IntegerField(default=0),
        ),
    ]
