# Generated by Django 2.2 on 2019-06-24 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("home", "0014_auto_20190607_0533")]

    operations = [
        migrations.CreateModel(
            name="popup",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("text", models.CharField(max_length=500)),
            ],
        )
    ]
