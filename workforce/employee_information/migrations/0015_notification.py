# Generated by Django 4.0.6 on 2023-03-14 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_information', '0014_employees_project_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('subject', models.CharField(max_length=255)),
                ('message', models.TextField(blank=True)),
            ],
        ),
    ]
