# Generated by Django 4.2 on 2023-04-05 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls_test', '0013_alter_tce_users_user_ip_alter_tce_users_user_otpkey_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tce_tests_users',
            name='testuser_comment',
            field=models.TextField(default=''),
        ),
    ]
