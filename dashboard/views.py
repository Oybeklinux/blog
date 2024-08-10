from django.shortcuts import get_object_or_404, redirect, render

from blogs.models import Blog, Category
from django.contrib.auth.decorators import login_required
from django.template.defaultfilters import slugify
from dashboard.forms import AddUserForm, BlogForm, CategoryForm, EditUserForm
from django.contrib.auth.models import User
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

def add_category(request):
    if request.method == "GET":
        form = CategoryForm()
        context = {
            "form": form
        }
        return render(request, "dashboard/add_category.html", context)
    elif request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
        return redirect('categories')
    
def edit_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'GET':
        form = CategoryForm(instance=category)
        context = {
            "form": form,
            "category": category
        }
        return render(request, "dashboard/edit_category.html", context)
    elif request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('categories')
        
def  delete_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    category.delete()
    return redirect('categories')

def blogs(request):
    blogs = Blog.objects.all()
    context = {
        "blogs": blogs
    }
    return render(request, "dashboard/blogs.html", context)

def add_blog(request):
    if request.method == "GET":
        form = BlogForm()
        context = {
            "form": form
        }
        return render(request, "dashboard/add_blog.html",context)
    else:
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user            
            blog.save()
            blog.slug = slugify(blog.title + str(blog.id))
            blog.save()
            return redirect('blogs')
        else:
            print(form.errors)


def users(request):
    users = User.objects.all()
    context = {
        "users": users
    }
    return render(request, "dashboard/users.html", context)


def add_user(request):
    if request.method == "GET":
        form = AddUserForm()
        context  = {
            "form": form
        }
        return render(request, "dashboard/add_user.html", context)
    else:
        form = AddUserForm(request.POST)
        if form.is_valid():
            form.save()            
        else:
            print(form.erros)
        return redirect('users')

def edit_user(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == "GET":
        form = EditUserForm(instance=user)
        context  = {
            "form": form
        }
        return render(request, "dashboard/edit_user.html", context)
    else:
        form = EditUserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()            
        else:
            print(form.errors)
        return redirect('users')
    

def  delete_user(request, pk):
    user = get_object_or_404(User, pk=pk)
    user.delete()
    return redirect('users')