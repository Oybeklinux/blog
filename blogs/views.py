from django.shortcuts import get_object_or_404, redirect, render

from blogs.models import Blog, Category

# Create your views here.

def posts_by_category(request, category_id):
    posts = Blog.objects.filter(category=category_id)
    # category = Category.objects.get(pk=category_id)
    # categories = Category.objects.all()
    category = get_object_or_404(Category, pk=category_id)
    context = {
        # "categories": categories,
        "posts": posts,
        "category": category
    }
    print(f"category_id", category_id)
    return render(request, "posts_by_category.html", context)