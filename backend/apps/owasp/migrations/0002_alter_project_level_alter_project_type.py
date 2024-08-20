# Generated by Django 5.1 on 2024-08-20 18:16

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("owasp", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="project",
            name="level",
            field=models.CharField(
                choices=[
                    ("other", "Other"),
                    ("incubator", "Incubator"),
                    ("lab", "Lab"),
                    ("production", "Production"),
                    ("flagship", "Flagship"),
                ],
                default="other",
                max_length=20,
                verbose_name="Level",
            ),
        ),
        migrations.AlterField(
            model_name="project",
            name="type",
            field=models.CharField(
                choices=[
                    ("code", "Code"),
                    ("documentation", "Documentation"),
                    ("other", "Other"),
                    ("tool", "Tool"),
                ],
                default="other",
                max_length=20,
                verbose_name="Type",
            ),
        ),
    ]