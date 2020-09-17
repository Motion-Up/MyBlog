from django.shortcuts import render, get_object_or_404
from .models import Post


# Create your views here.

def showblog(request):
    '''Делает перезод на страницу блога и возвращает содежимое из БД'''

    posts = Post.objects
    return render(request, 'blog/blog.html', {'posts': posts})

def specific_post(request, post_id):
    '''Делает переход на страницу выбранного блога'''

    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'blog/specific_post.html', {'post': post})







