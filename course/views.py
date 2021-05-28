from django.shortcuts import render,redirect
from course.models import courses
from django.contrib import messages
# Create your views here.
def courseshome(request):
    allCourse=courses.objects.all()
    context={'allCourse':allCourse}
    return render(request,'course/courseshome.html',context)
def coursesview(request,slug):
    course=courses.objects.filter(slug=slug).first()
    context={'course':course,'user':request.user}
    return render(request,'course/coursesview.html',context)
