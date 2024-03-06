from django.http.response import HttpResponse 
from django.shortcuts import render,redirect
from .models import Post
from datetime import datetime

def homepage(request):
    posts = Post.objects.all()
    now = datetime.now()
    # post_list = list()
    # for count,post in enumerate(posts):
    #     post_list.append(f"No.{count} {str(post)} <hr>")
    #     post_list.append(f"<small> {post.body} </small><br/><br/> ")
    # return HttpResponse(post_list)
    return render(request,'index.html',locals())

def showpost(request,slug):
    try:
        post = Post.objects.get(slug=slug)
        if post!=None:
            return render(request,"post.html",locals())
    except:
        return redirect("/")


