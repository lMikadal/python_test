# Generated by Django 4.2.2 on 2023-06-16 17:03

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("app_main", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Goods",
            new_name="Good",
        ),
    ]