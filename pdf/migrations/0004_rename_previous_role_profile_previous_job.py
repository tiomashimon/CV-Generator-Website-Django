# Generated by Django 4.2.3 on 2023-07-25 11:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pdf', '0003_rename_previous_job_profile_previous_role'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='previous_role',
            new_name='previous_job',
        ),
    ]
