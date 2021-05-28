from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.
class Ebook(models.Model):
    sno=models.AutoField(primary_key=True)
    title=models.CharField(max_length=50)
    content=RichTextUploadingField(blank=True)
    category=models.CharField(max_length=255, default='')
    credit=models.CharField(max_length=100, blank=True)

    def __str__(self):
        return 'Ebook on '+self.title