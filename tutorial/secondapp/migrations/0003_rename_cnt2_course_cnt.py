# Generated by Django 4.1 on 2024-04-12 00:32

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("secondapp", "0002_rename_cnt_course_cnt2"),
    ]

    operations = [
        migrations.RenameField(
            model_name="course",
            old_name="cnt2",
            new_name="cnt",
        ),
    ]
