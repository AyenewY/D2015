# Generated by Django 4.2 on 2023-04-12 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls_test', '0026_taken_crsstsid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taken',
            name='taken_year',
            field=models.PositiveIntegerField(default=2023, verbose_name='Academic Year'),
        ),
    ]
