# Generated by Django 5.0.6 on 2024-07-08 18:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_accountsettings_chartofaccount_rulesregulations'),
        ('fees', '0001_initial'),
        ('student', '0002_admissionletter_basiclist_promotestudent_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student_Fee_Challan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date_paid', models.DateField()),
                ('fee_month', models.CharField(max_length=50)),
                ('due_date', models.DateField()),
                ('fine_after_due_date', models.DecimalField(decimal_places=2, max_digits=10)),
                ('bank_copy', models.BooleanField(default=False)),
                ('student_copy', models.BooleanField(default=False)),
                ('institute_copy', models.BooleanField(default=False)),
                ('bank', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fees.bank_fee_challan')),
                ('chart_of_account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.chartofaccount')),
                ('particulars', models.ManyToManyField(to='fees.feeparticulars')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.student')),
            ],
        ),
    ]
