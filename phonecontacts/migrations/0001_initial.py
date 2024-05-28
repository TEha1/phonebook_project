# Generated by Django 4.2.13 on 2024-05-28 08:02

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Contact",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="the name of the contact",
                        max_length=255,
                        verbose_name="name",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="PhoneNumber",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "number",
                    phonenumber_field.modelfields.PhoneNumberField(
                        max_length=128, region=None
                    ),
                ),
                (
                    "contact",
                    models.ForeignKey(
                        help_text="the contact of the phone",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="phone_numbers",
                        to="phonecontacts.contact",
                        verbose_name="contact",
                    ),
                ),
            ],
        ),
    ]