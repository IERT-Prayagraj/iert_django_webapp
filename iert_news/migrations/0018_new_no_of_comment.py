# Generated by Django 2.1.5 on 2019-03-02 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("iert_news", "0017_auto_20190302_2058")]

    operations = [
        migrations.AddField(
            model_name="new", name="no_of_comment", field=models.IntegerField(null=True)
        )
    ]
