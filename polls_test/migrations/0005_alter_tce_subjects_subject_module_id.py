# Generated by Django 4.1.7 on 2023-04-01 12:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls_test', '0004_tce_questions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tce_subjects',
            name='subject_module_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='polls_test.tce_modules'),
        ),
    ]
