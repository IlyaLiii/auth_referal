# Generated by Django 3.2 on 2023-08-23 06:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('referal', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='invite_user',
            new_name='inviting_user',
        ),
    ]
