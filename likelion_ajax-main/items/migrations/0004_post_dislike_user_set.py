# Generated by Django 4.0.6 on 2022-07-26 09:36

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0001_initial'),
        ('items', '0003_dislike'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='dislike_user_set',
            field=models.ManyToManyField(blank=True, related_name='dislikes_user_set', through='items.Dislike', to=settings.AUTH_USER_MODEL),
        ),
    ]
