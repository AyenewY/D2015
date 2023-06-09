# Generated by Django 4.1.7 on 2023-04-01 10:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls_test', '0002_tce_sessions_tce_users'),
    ]

    operations = [
        migrations.CreateModel(
            name='tce_modules',
            fields=[
                ('module_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('module_name', models.CharField(default='CSE', max_length=255, unique=True)),
                ('module_enabled', models.BooleanField(default=False)),
                ('module_user_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='polls_test.tce_users')),
            ],
        ),
        migrations.CreateModel(
            name='tce_subjects',
            fields=[
                ('subject_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('subject_name', models.CharField(max_length=255, unique=True)),
                ('subject_description', models.TextField(default='')),
                ('subject_enabled', models.BooleanField(default=False)),
                ('subject_module_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='polls_test.tce_modules', unique=True)),
                ('subject_user_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='polls_test.tce_users')),
            ],
        ),
    ]
