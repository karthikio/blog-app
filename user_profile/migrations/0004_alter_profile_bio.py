# Generated by Django 3.2.4 on 2021-06-23 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0003_alter_profile_privacy'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.TextField(blank=True, default="Hey, I'm using blog app", max_length=500, null=True),
        ),
    ]
