# Generated by Django 2.2.16 on 2022-05-21 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20220520_2048'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='follow',
            name='detection_user_author',
        ),
        migrations.RenameField(
            model_name='follow',
            old_name='author',
            new_name='following',
        ),
        migrations.AddConstraint(
            model_name='follow',
            constraint=models.UniqueConstraint(fields=('user', 'following'), name='detection_user_following'),
        ),
    ]