# Generated by Django 4.2 on 2023-04-12 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls_test', '0029_contract_employee_alter_taken_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='permanent_employee',
            fields=[
                ('employee_name', models.CharField(max_length=100)),
                ('employee_id', models.CharField(max_length=25, primary_key=True, serialize=False)),
                ('employee_age', models.PositiveIntegerField(default=20)),
                ('employee_salary', models.FloatField(default=2500.0, verbose_name='Employee Salary ')),
                ('pension_rate', models.FloatField(default=0.05)),
                ('retire_age', models.PositiveSmallIntegerField(default=60)),
            ],
            options={
                'db_table': 'per_employee',
                'abstract': False,
            },
        ),
    ]
