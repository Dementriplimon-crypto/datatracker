# Generated by Django 4.2.16 on 2024-10-24 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("person", "0002_alter_historicalperson_ascii_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="personalapikey",
            name="endpoint",
            field=models.CharField(
                choices=[
                    ("/api/appauth/authortools", "/api/appauth/authortools"),
                    ("/api/appauth/bibxml", "/api/appauth/bibxml"),
                    ("/api/iesg/position", "/api/iesg/position"),
                    (
                        "/api/meeting/session/recording-name",
                        "/api/meeting/session/recording-name",
                    ),
                    (
                        "/api/meeting/session/video/url",
                        "/api/meeting/session/video/url",
                    ),
                    ("/api/notify/meeting/bluesheet", "/api/notify/meeting/bluesheet"),
                    (
                        "/api/notify/meeting/registration",
                        "/api/notify/meeting/registration",
                    ),
                    ("/api/notify/session/attendees", "/api/notify/session/attendees"),
                    ("/api/notify/session/chatlog", "/api/notify/session/chatlog"),
                    ("/api/notify/session/polls", "/api/notify/session/polls"),
                    ("/api/v2/person/person", "/api/v2/person/person"),
                ],
                max_length=128,
            ),
        ),
    ]
