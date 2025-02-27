# Generated by Django 5.0.6 on 2024-07-08 19:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('staff', '0002_liveclass_jobletter_salary_staffidcard'),
        ('student', '0003_student_fee_challan'),
    ]

    operations = [
        migrations.CreateModel(
            name='SMS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipient_number', models.CharField(max_length=15)),
                ('message', models.TextField()),
                ('date_sent', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Messaging',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('date_sent', models.DateField()),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receiver', to='staff.staff')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sender', to='staff.staff')),
            ],
        ),
        migrations.CreateModel(
            name='WhatsApp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('date_sent', models.DateField()),
                ('communication_type', models.CharField(choices=[('All Teachers', 'All Teachers'), ('All Students', 'All Students'), ('Specific Teacher', 'Specific Teacher'), ('Specific Student', 'Specific Student')], default='All Teachers', max_length=20)),
                ('staff', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='staff.staff')),
                ('student', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='student.student')),
            ],
        ),
    ]
