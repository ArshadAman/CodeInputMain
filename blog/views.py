from django.shortcuts import render,HttpResponse,redirect
from blog.models import Post,BlogComment
from django.contrib import messages
# Create your views here.
def blogHome(request):
    allPosts=Post.objects.all()
    context={'allPosts':allPosts}
    return render(request,'blog/blogHome.html',context)
def Nones(request):
    return render(request,'blog/none.html')
def blogPost(request,slug):
    post=Post.objects.filter(slug=slug).first()
    comments=BlogComment.objects.filter(post=post, parent=None)
    post.views=post.views + 1
    post.save()
    # replies=BlogComment.objects.filter(post=post).exclude(parent=None)
    # replyDict={}

    # for reply in replies:
    #     if reply.sno not in replyDict.keys():
    #         replyDict[reply.parent.sno]=[reply]
    #     else:
    #         replyDict[reply.parent.sno].append(reply)
    
    context={'post':post,'comments':comments,'user':request.user}
    return render(request,'blog/blogPost.html',context)


def postComment(request):
    if request.method=="POST":
        comment=request.POST.get("comment")
        user=request.user
        postSno=request.POST.get("postSno")
        post=Post.objects.get(sno=postSno)
        parentSno=request.POST.get("parentSno")
        comment=BlogComment(comment=comment,user=user,post=post)
        comment.save()
        messages.success(request, " Your Comment has been Posted")

        # else:
        #     parent=BlogComment.objects.get(sno=parentSno)
        #     comment=BlogComment(comment=comment,user=user,post=post, parent=parent)
        #     comment.save()
        #     messages.success(request, " You have replied...")
    return redirect(f"/blog/{post.slug}")

