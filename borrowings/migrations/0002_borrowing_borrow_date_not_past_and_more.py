# Generated by Django 5.0 on 2023-12-08 11:17

import datetime
import django.db.models.expressions
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("books", "0001_initial"),
        ("borrowings", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddConstraint(
            model_name="borrowing",
            constraint=models.CheckConstraint(
                check=models.Q(("borrow_date__gte", datetime.date(2023, 12, 8))),
                name="borrow_date_not_past",
            ),
        ),
        migrations.AddConstraint(
            model_name="borrowing",
            constraint=models.CheckConstraint(
                check=models.Q(
                    (
                        "expected_return_date__lte",
                        django.db.models.expressions.CombinedExpression(
                            models.F("borrow_date"),
                            "+",
                            models.Value(datetime.timedelta(days=14)),
                        ),
                    )
                ),
                name="expected_return_date_within_two_weeks",
            ),
        ),
    ]