# Generated by Django 4.0.6 on 2023-02-26 19:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employee_information', '0013_remove_employees_project_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='employees',
            name='project_id',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='employee_information.project'),
            preserve_default=False,
        ),
    ]
