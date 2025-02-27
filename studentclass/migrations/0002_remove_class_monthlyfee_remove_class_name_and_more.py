# Generated by Django 5.0.6 on 2024-07-08 17:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_instituteprofile'),
        ('student', '0002_admissionletter_basiclist_promotestudent_and_more'),
        ('studentclass', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='class',
            name='monthlyFee',
        ),
        migrations.RemoveField(
            model_name='class',
            name='name',
        ),
        migrations.RemoveField(
            model_name='class',
            name='teacher',
        ),
        migrations.RemoveField(
            model_name='subject',
            name='teahcer',
        ),
        migrations.RemoveField(
            model_name='subject',
            name='totalMarks',
        ),
        migrations.AddField(
            model_name='class',
            name='Class_name',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='class',
            name='Select_Class_Teacher',
            field=models.CharField(choices=[('irfan', 'irfan'), ('abbas', 'abbas'), ('bilal', 'bilal')], default='irfan', max_length=5),
        ),
        migrations.AddField(
            model_name='class',
            name='institute',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='accounts.instituteprofile'),
        ),
        migrations.AddField(
            model_name='class',
            name='monthly_tution_fee',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='subject',
            name='classes',
            field=models.ManyToManyField(related_name='subjects', to='studentclass.class'),
        ),
        migrations.AlterField(
            model_name='subject',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.CreateModel(
            name='ClassTest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('class_assigned', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studentclass.class')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studentclass.subject')),
            ],
        ),
        migrations.CreateModel(
            name='TestResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marks_obtained', models.IntegerField()),
                ('class_test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studentclass.classtest')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.student')),
            ],
        ),
    ]
