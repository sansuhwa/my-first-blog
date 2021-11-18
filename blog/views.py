from django.shortcuts import render, get_object_or_404
from .models import Post
from django.utils import timezone


def post_list(requset):
    qs = Post.objects.all()
    qs = qs.filter(published_date__lte=timezone.now())
    qs = qs.order_by('published_date')

    return render(requset, 'blog/post_list.html', {
        'post_list': qs,
    })

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    context = {
        'post': post
    }
    return render(request, 'blog/post_detail.html', context=context)
