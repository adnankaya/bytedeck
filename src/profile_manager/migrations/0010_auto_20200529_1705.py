# Generated by Django 2.2.12 on 2020-05-30 00:05

from django.db import migrations
import profile_manager.models
import utilities.models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_manager', '0009_auto_20200425_2052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='custom_stylesheet',
            field=utilities.models.RestrictedFileField(blank=True, help_text='ADVANCED: A CSS file to customize this site!  You can use                                                     this to tweak something, or create a completely new theme.', null=True, upload_to=profile_manager.models.user_directory_path),
        ),
    ]