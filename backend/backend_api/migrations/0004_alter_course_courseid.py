# Generated by Django 4.1.4 on 2022-12-19 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend_api', '0003_alter_course_semester_alter_course_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='courseid',
            field=models.CharField(max_length=255),
        ),
    ]
