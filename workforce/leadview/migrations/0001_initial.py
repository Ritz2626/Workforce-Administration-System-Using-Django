# Generated by Django 4.0.6 on 2023-03-19 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='files',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_id1', models.CharField(max_length=255)),
                ('file_uploaded', models.FileField(upload_to='media')),
            ],
        ),
    ]
