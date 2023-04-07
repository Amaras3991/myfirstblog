from django.shortcuts import render, get_object_or_404, redirect
from .models import Post

def index(request):
    posts = Post.objects.all()
    context = {'post_list': posts}
    return render(request, 'blog/index.html', context)

def result(request, pk):
    post = get_object_or_404(Post, id=pk)
    return render(request, 'blog/result.html', {'post': post})


def addComments(request, pk):
    print(request.POST)
    return redirect('/')



