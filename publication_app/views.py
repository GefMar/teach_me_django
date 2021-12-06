from django.shortcuts import render, redirect

from .forms.registrations import RegistrationForm
from .models import Post


def main_page(request):
    posts = Post.objects.filter(is_public=True).order_by("-create_date", "-id").all()
    context = {'title': "ПРИВЕТ МИР", "posts": posts}
    return render(request, 'mainpage.html', context)


def registration_page(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            instance = form.save()
            return redirect("/")
    else:
        form = RegistrationForm()
    context = {
        'reg_form': form
    }
    return render(request, "reg_form.html", context)
