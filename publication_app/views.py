from django.shortcuts import render
from .models import Post


def main_page(request):
    posts = Post.objects.filter(is_public=True).order_by("-create_date", "-id").all()
    context = {'title': "ПРИВЕТ МИР", "posts": posts}
    return render(request, 'mainpage.html', context)
