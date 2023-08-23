from django.shortcuts import render, redirect
from .models import Post

# Create your views here.
# Read 관련 함수
def index(request):
    posts = Post.objects.all()
    
    context = {
        'posts': posts
    }

    return render(request,'index.html',context)

def detail(request, id):
    post = Post.objects.get(id=id)
    
    context = {
        'post': post,
    }
    
    return render(request, 'detail.html', context)

# Create 관련 함수
def new(request):
    return render(request, 'new.html')

def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    
#    post = Post()
#    post.title = title
#    post.content = content
#    post.save()
    
    post = Post(title=title, content=content)
    post.save()
    
    return redirect('posts:detail', id=post.id)

# Delete 관련 함수
def delete(request, id):
    post = Post.objects.get(id=id)
    post.delete()
    
    return redirect('posts:index')

# Update 관련 함수
def edit(request, id):
    post = Post.objects.get(id=id)
    
    context = {
        'post': post,
    }
    
    return render(request, 'edit.html', context)

def update(request, id):
    # new data
    title = request.POST.get('title')
    content = request.POST.get('content')
    
    # old data
    post = Post.objects.get(id=id)
    post.title = title
    post.content = content
    post.save()
    
    return redirect('posts.detail', id=post.id)