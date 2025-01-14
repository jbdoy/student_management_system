# Generated by Django 5.0.2 on 2024-04-12 16:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0005_course_instructor_enrollment_grade_course_instructor'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='days_of_week',
            field=models.CharField(blank=True, max_length=7, null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='end_time',
            field=models.TimeField(default=datetime.time(10, 30)),
        ),
        migrations.AddField(
            model_name='course',
            name='start_time',
            field=models.TimeField(default=datetime.time(9, 0)),
        ),
    ]
