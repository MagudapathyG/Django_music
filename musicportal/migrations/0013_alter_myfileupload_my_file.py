# Generated by Django 4.2.1 on 2023-05-30 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicportal', '0012_alter_myfileupload_my_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myfileupload',
            name='my_file',
            field=models.FileField(help_text='.mp3 supported only', upload_to='uploads/'),
        ),
    ]
