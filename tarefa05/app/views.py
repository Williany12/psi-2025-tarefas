from django.shortcuts import render, get_object_or_404
from .models import Post, Blog



def index(request):
    context = {
        'posts': Post.objects.all(),
        'blog': Blog.objects.first(),
    }
    return render(request, 'app/index.html',context)

def post(request,id_post):
    postagem = get_object_or_404(Post, id=id_post)
    context = {
        'posts': postagem,
        'blog': Blog.objects.first(),
    }
    return render(request, 'app/post.html',context)
