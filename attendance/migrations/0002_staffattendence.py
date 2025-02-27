# Generated by Django 5.0.6 on 2024-07-08 16:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0001_initial'),
        ('staff', '0001_initial'),
        ('studentclass', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StaffAttendence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('attendence', models.CharField(choices=[('P', 'P'), ('L', 'L'), ('A', 'A')], max_length=1)),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attendence', to='staff.staff')),
                ('studentClass', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='staff_attendence', to='studentclass.class')),
            ],
            options={
                'unique_together': {('staff', 'studentClass', 'date')},
            },
        ),
    ]
