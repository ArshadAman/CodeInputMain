from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.
class courses(models.Model):
    sno=models.AutoField(primary_key=True)
    title=models.CharField(max_length=50)
    content=RichTextUploadingField(blank=True)
    slug=models.CharField(max_length=100, default='')
    category=models.CharField(max_length=255, default='')
    youtube_channel=models.CharField(max_length=100)
    playlist_id=models.CharField(max_length=300,default='')


    def __str__(self):
        return self.title+' by '+self.youtube_channel

            