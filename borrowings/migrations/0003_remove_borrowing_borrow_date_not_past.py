# Generated by Django 5.0 on 2023-12-11 13:27

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("borrowings", "0002_borrowing_borrow_date_not_past_and_more"),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name="borrowing",
            name="borrow_date_not_past",
        ),
    ]
