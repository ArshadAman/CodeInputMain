from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Contact(models.Model):
    sno=models.AutoField(primary_key=True)
    name=models.CharField(max_length=255)
    phone=models.CharField(max_length=13)
    email=models.CharField(max_length=100)
    socialmedia=models.URLField(max_length=250, default='')
    content=models.TextField()
    timeStamp=models.DateTimeField(auto_now_add=True,blank=True)


    def __str__(self):
        return 'Message from '+ self.name+' - '+self.email


    