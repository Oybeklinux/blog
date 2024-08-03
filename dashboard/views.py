from django.shortcuts import render

from blogs.models import Blog, Category
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required(login_url='login')
def dashboard(request):
    blog_count = Blog.objects.all().count()
    category_count = Category.objects.all().count()
    context = {
        "blog_count": blog_count,
        "category_count": category_count
    }
    return render(request, "dashboard/dashboard.html", context)


def categories(request):
    return render(request, "dashboard/categories.html")