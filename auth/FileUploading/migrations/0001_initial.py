# Generated by Django 4.2.1 on 2023-10-03 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.CharField(max_length=100)),
                ('file_description', models.TextField()),
                ('file_image', models.ImageField(upload_to='my_file')),
            ],
        ),
    ]
