# Generated by Django 2.1 on 2018-08-20 19:14

from django.db import migrations
from django.contrib.auth.models import User


def create_auth_user(apps, schema_editor):
    admin_user = User.objects.create_user(
        'admin',
        'j23schoen@gmail.com',
        'password',
        is_superuser=True,
        is_staff=True
    )
    admin_user.save()


class Migration(migrations.Migration):

    dependencies = [
        ('lift', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_auth_user)
    ]
