# Generated by Django 4.2 on 2023-04-11 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls_test', '0017_alter_tce_tests_test_repeatable'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tce_tests',
            name='test_password',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
    ]
