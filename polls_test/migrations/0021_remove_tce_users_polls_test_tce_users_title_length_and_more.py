# Generated by Django 4.2 on 2023-04-11 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls_test', '0020_remove_tce_tests_polls_test_tce_tests_title_length_and_more'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='tce_users',
            name='polls_test_tce_users_title_length',
        ),
        migrations.AddConstraint(
            model_name='tce_users',
            constraint=models.CheckConstraint(check=models.Q(('user_password__length__gte', 8)), name='polls_test_tce_users_users_length'),
        ),
    ]
