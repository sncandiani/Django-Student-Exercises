# Generated by Django 3.0.6 on 2020-05-07 18:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schoolapp', '0003_student'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='cohort_id',
            new_name='cohort',
        ),
    ]
