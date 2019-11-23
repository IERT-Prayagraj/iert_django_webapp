# Generated by Django 2.1.5 on 2019-02-11 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("iert_news", "0005_auto_20190211_1640")]

    operations = [
        migrations.AlterField(
            model_name="new", name="date", field=models.DateField(blank=True, null=True)
        ),
        migrations.AlterField(
            model_name="new",
            name="image",
            field=models.ImageField(
                blank=True, default="", null=True, upload_to="media/"
            ),
        ),
        migrations.AlterField(
            model_name="new_by_viewer",
            name="date",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="new_by_viewer",
            name="image",
            field=models.ImageField(
                blank=True, default="", null=True, upload_to="media/"
            ),
        ),
    ]
