# Generated by Django 5.1 on 2024-08-20 20:44

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("github", "0007_user_repository_owner"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="organization",
            name="is_verified",
        ),
    ]