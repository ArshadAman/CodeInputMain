from django.shortcuts import render
from ebook.models import Ebook
# Create your views here.
def ebook(request):
    allEbook=Ebook.objects.all()
    context={'allEbook':allEbook}
    return render(request,'ebook/ebook.html',context)