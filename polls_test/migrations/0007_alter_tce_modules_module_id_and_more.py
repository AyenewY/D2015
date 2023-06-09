# Generated by Django 4.1.7 on 2023-04-03 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls_test', '0006_tce_answers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tce_modules',
            name='module_id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='tce_questions',
            name='question_id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='tce_subjects',
            name='subject_id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='tce_users',
            name='user_id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False),
        ),
    ]
