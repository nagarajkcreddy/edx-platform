# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-02-26 21:20


import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('program_enrollments', '0008_add_ended_programenrollment_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='programcourseenrollment',
            name='course_enrollment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='student.CourseEnrollment'),
        ),
    ]
