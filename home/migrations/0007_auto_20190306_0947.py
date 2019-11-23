# Generated by Django 2.1.5 on 2019-03-06 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("home", "0006_notice")]

    operations = [
        migrations.DeleteModel(name="notice"),
        migrations.RenameField(
            model_name="degree_detail",
            old_name="timetable",
            new_name="timetable_1_year",
        ),
        migrations.AddField(
            model_name="degree_detail",
            name="timetable_2_year",
            field=models.TextField(default=""),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="degree_detail",
            name="timetable_3_year",
            field=models.TextField(default=" "),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="degree_detail",
            name="timetable_4_year",
            field=models.TextField(default=" "),
            preserve_default=False,
        ),
    ]
