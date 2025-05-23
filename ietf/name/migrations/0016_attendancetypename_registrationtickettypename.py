# Generated by Django 4.2.17 on 2025-01-02 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("name", "0015_last_call_name"),
    ]

    operations = [
        migrations.CreateModel(
            name="AttendanceTypeName",
            fields=[
                (
                    "slug",
                    models.CharField(max_length=32, primary_key=True, serialize=False),
                ),
                ("name", models.CharField(max_length=255)),
                ("desc", models.TextField(blank=True)),
                ("used", models.BooleanField(default=True)),
                ("order", models.IntegerField(default=0)),
            ],
            options={
                "ordering": ["order", "name"],
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="RegistrationTicketTypeName",
            fields=[
                (
                    "slug",
                    models.CharField(max_length=32, primary_key=True, serialize=False),
                ),
                ("name", models.CharField(max_length=255)),
                ("desc", models.TextField(blank=True)),
                ("used", models.BooleanField(default=True)),
                ("order", models.IntegerField(default=0)),
            ],
            options={
                "ordering": ["order", "name"],
                "abstract": False,
            },
        ),
    ]
