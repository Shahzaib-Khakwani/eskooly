# Generated by Django 5.0.6 on 2024-07-08 18:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_instituteprofile_alter_gradingsystem_institute_and_more'),
        ('studentclass', '0002_remove_class_monthlyfee_remove_class_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class',
            name='institute',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='myapp.instituteprofile'),
        ),
    ]
