# Generated by Django 2.2.13 on 2020-09-08 02:33

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('profile_manager', '0014_auto_20200819_1834'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format=None, keep_meta=True, null=True, quality=90, size=[256, 256], upload_to='avatars/'),
        ),
    ]