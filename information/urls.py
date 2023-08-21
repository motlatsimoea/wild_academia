from django.urls import path
from .views import information, category, ArticleDetails, label

urlpatterns  = [
    path('', information, name='information'),
    path('categories/<slug:category_slug>', category, name='category'),
    path('labels/<slug:label_slug>', label, name='labels'),
    path('<slug:article_slug>', ArticleDetails, name='article_details'),
]