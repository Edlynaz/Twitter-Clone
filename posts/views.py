from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import Post
from .forms import PostForm



def index(request):
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect(form.erros.as_json())

    posts = Post.objects.all().order_by('-created_at')[:20]

    return render(request, 'post.html',
                  {'posts': posts})

def delete(request, post_id):
    post = Post.objects.get(id = post_id)
    post.delete()
    return HttpResponseRedirect('/')


def edit(request, post_id):
    post = Post.objects.get(id=post_id)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')

        else:

            return HttpResponseRedirect(form.erros.as_json())
    return render(request, "edit.html", {"post": post})


def likebtn(request, post_id):
    like=Post.objects.get(id = post_id)
    like.likes += 1
    like.save()
    return HttpResponseRedirect('/')



