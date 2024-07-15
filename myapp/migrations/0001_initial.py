# Generated by Django 5.0.6 on 2024-07-08 15:05

import django.core.validators
import django.db.models.deletion
import django_countries.fields
import myapp.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=300)),
                ('accountNumber', models.PositiveIntegerField()),
                ('image', models.ImageField(upload_to=myapp.models.image_bank_path)),
                ('instructions', models.TextField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='banks', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='GradingSystem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.CharField(max_length=2)),
                ('fromPercentage', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('toPercentage', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('status', models.CharField(max_length=4)),
                ('gradingSystem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='grades', to='myapp.gradingsystem')),
            ],
        ),
        migrations.CreateModel(
            name='FailCriteria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('overAllPercentage', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('subjectAllPercentage', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('noSubject', models.PositiveIntegerField()),
                ('gradingSystem', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='fail_criteria', to='myapp.gradingsystem')),
            ],
        ),
        migrations.CreateModel(
            name='Institute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=300)),
                ('phoneNumber', models.PositiveIntegerField()),
                ('websiteUrl', models.URLField(blank=True, null=True)),
                ('targetLine', models.CharField(max_length=600)),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('image', models.ImageField(upload_to=myapp.models.image_institute_path)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='institutes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='gradingsystem',
            name='institute',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='grading_system', to='myapp.institute'),
        ),
        migrations.CreateModel(
            name='Rule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rule', models.TextField()),
                ('institute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Rules', to='myapp.institute')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
