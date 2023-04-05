# Generated by Django 4.1.7 on 2023-04-03 08:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls_test', '0005_alter_tce_subjects_subject_module_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='tce_answers',
            fields=[
                ('answer_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('answer_description', models.TextField(max_length=500, null=True)),
                ('answer_explanation', models.TextField(null=True)),
                ('answer_isright', models.BooleanField(default=0)),
                ('answer_enabled', models.BooleanField(default=0)),
                ('answer_position', models.BigIntegerField(null=True)),
                ('answer_keyboard_key', models.SmallIntegerField(null=True)),
                ('answer_question_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls_test.question')),
            ],
        ),
    ]
