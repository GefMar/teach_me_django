from django.contrib.auth import authenticate, login
# from django.contrib.auth.decorators import login_required
from django.db.models import Q, F
from django.shortcuts import render, redirect
from django.views.generic import ListView

from .forms.auth import AuthForm
from .forms.registrations import RegistrationForm
from .models import Post


def main_page(request):
    q_filters = Q(is_public=True, )
    posts = Post.objects.filter(q_filters).order_by("-create_date", "-id").all()
    main_menu = []
    context = {'title': "ПРИВЕТ МИР", "posts": posts, "user": request.user}
    return render(request, 'mainpage.html', context)


class PostListView(ListView):
    queryset = Post.objects.all()
    template_name = 'mainpage.html'
    context_object_name = 'posts'
    ordering = ("-create_date", "-id")
    http_method_names = ['get', ]
    form_class = RegistrationForm

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return self.queryset.all()
        return self.queryset.filter(is_public=True).all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['title'] = "Супер ПОСТЫ"
        context['user'] = self.request.user
        return context

    def get(self, request, *args, **kwargs):
        result = super().get(request, *args, **kwargs)
        return result


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
