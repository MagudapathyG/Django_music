# Generated by Django 4.2.1 on 2023-05-29 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicportal', '0008_alter_myfileupload_my_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myfileupload',
            name='my_file',
            field=models.FileField(upload_to='audio/'),
        ),
    ]
