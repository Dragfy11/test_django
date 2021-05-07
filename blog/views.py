from django.shortcuts import render
from .models import Article

def blog_index(request):
    articles = Article.objects.all()
    data = {'articles': articles}
    return render(request, 'blog/blog_index.html', data)

def article(request, name):
    return render(request, 'blog/article.html')
