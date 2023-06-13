from django.db import models

# Create your models here.

class MyFileUpload(models.Model):
    file_name=models.CharField(max_length=50)
    my_file=models.FileField(upload_to='uploads/',help_text=".mp3 supported only")
    image=models.ImageField(upload_to="static/images",default='')
    
