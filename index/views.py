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
    return render(request, 'category.html')

def get_news(request):
    return render(request, 'news.html')

def search_news(request):
    if request.method == 'POST':
        get_product = request.POST.get('search_news')

        try:
            exact_product = News.objects.get(pr_name__icontains=get_product)
            return redirect(f'product/{exact_product.id}')
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