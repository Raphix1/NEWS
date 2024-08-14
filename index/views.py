from django.shortcuts import render, redirect
from .models import NewsCategory, News
from django.views import View
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from .forms import RegisterForm

def home_page(request):
    view_news = News.objects.all()
    view_categ = NewsCategory.objects.all()

    context = {'view_news': view_news,
               'view_categ': view_categ}
    return render(request, 'home.html', context)

def get_category(request):
    exact_category = NewsCategory.objects.get1

    context = {'ecat': exact_category}
    return render(request, 'category.html', context)

def get_news(request, pk):
    exact_news = News.objects.get(id=pk)

    # Передаем данные на фронт
    context = {'enews': exact_news}
    return render(request, 'news.html', context)

def search_news(request):
    if request.method == 'POST':
        get_news = request.POST.get('search_news')

        try:
            exact_news = News.objects.get(head__icontains=get_news)
            return redirect(f'news/{exact_news.id}')
        except:
            print('не нашел')
            return redirect('/')

class Register(View):
    template_name = 'registration/register.html'


    def get(self, request):
        context = {'form': RegisterForm}
        return render(request, self.template_name, context)


    def post(self, request):
        form = RegisterForm(request.POST)

        if form.is_valid():
            username = form.clean_username()
            password2 = form.cleaned_data.get("password2")
            email = form.cleaned_data.get("email")
            user = User.objects.create_user(username, password=password2, email=email)
            print(username, password2, email)
            user.save()
            login(request, user)
            return redirect('/')
        context = {'form': RegisterForm}
        return render(request, self.template_name, context)


def logout_view(request):
    logout(request)
    return redirect('/')