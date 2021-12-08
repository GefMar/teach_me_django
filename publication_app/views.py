from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from .forms.auth import AuthForm
from .forms.registrations import RegistrationForm
from .models import Post


def main_page(request):
    posts = Post.objects.filter(is_public=True).order_by("-create_date", "-id").all()
    main_menu = []
    context = {'title': "ПРИВЕТ МИР", "posts": posts, "user": request.user}
    return render(request, 'mainpage.html', context)


def registration_page(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = RegistrationForm()
    context = {
        'reg_form': form
    }
    return render(request, "reg_form.html", context)


def auth_page(request):
    error = False
    if request.method == "POST":
        form = AuthForm(request.POST)
        if form.is_valid():
            user = authenticate(request, **form.cleaned_data)
            if user is not None:
                login(request, user)
                next_page = request.GET.get("next", "/")
                return redirect(next_page)
            error = True
    else:
        form = AuthForm()
    context = {"auth_form": form, "error": error}
    return render(request, "auth_form.html", context)
