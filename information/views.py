from django.shortcuts import render, get_object_or_404
from .models import Article, Category, Label
from django.contrib.auth.decorators import login_required


@login_required
def information(request):
    categories  = Category.objects.all()
    articles    = Article.objects.filter(status='published').order_by('-date_posted')

    context = {
        'categories': categories,
        'articles': articles,
    }

    return render(request, 'information/landing.html', context)



@login_required
def category(request, category_slug):
    articles     = Article.objects.filter(status='published').order_by('-date_posted')
    categories   = Category.objects.all() 

    if category_slug:
        category    = get_object_or_404(Category, slug=category_slug)
        articles    = articles.filter(category=category)



    context = {
        'articles' : articles,
        'categories': categories,
    }

    return render(request, 'information/categories.html', context)




@login_required   
def label(request, label_slug):
    labels         = Label.objects.all()
    articles       = Article.objects.filter(status='published').order_by('-date_posted')

    if label_slug:
        label         = get_object_or_404(Label, slug=label_slug)
        articles    = articles.filter(labels=label)

    context = {
        'articles': articles,
        'tags': labels,    
    }

    return render(request, 'information/labels.html', context)


@login_required
def ArticleDetails(request, article_slug):
    article         = get_object_or_404(Article, slug=article_slug)
    categories     = Category.objects.all()

    context = {
        'article': article,
        'categories': categories,
    }


    return render(request,'information/article_details.html', context)