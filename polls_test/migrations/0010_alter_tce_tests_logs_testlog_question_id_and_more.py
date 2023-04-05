# Generated by Django 4.1.7 on 2023-04-03 12:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls_test', '0009_tce_sslcerts_tce_test_subject_set_tce_tests_logs_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tce_tests_logs',
            name='testlog_question_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='polls_test.tce_questions'),
        ),
        migrations.AlterField(
            model_name='tce_tests_logs',
            name='testlog_testuser_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='polls_test.tce_tests_users'),
        ),
        migrations.AlterField(
            model_name='tce_tests_users',
            name='testuser_test_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='polls_test.tce_tests'),
        ),
        migrations.AlterField(
            model_name='tce_tests_users',
            name='testuser_user_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='polls_test.tce_users'),
        ),
        migrations.AlterField(
            model_name='tce_tsets_users',
            name='testuser_test_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='polls_test.tce_tests'),
        ),
        migrations.AlterField(
            model_name='tce_tsets_users',
            name='testuser_user_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='polls_test.tce_users'),
        ),
    ]