# Generated by Django 4.1.1 on 2023-04-20 09:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls_test', '0032_employee_salary_emp_collection_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='retired_employee',
            options={'managed': True, 'verbose_name': 'RetiredEmployee', 'verbose_name_plural': 'RetiredEmployees'},
        ),
        migrations.AlterModelTable(
            name='retired_employee',
            table='Retired Employee',
        ),
    ]
