# Generated by Django 2.1.5 on 2019-02-20 17:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [("extra_links", "0001_initial")]

    operations = [
        migrations.AddField(
            model_name="notice_board",
            name="date",
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        )
    ]
