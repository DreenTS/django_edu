from django.urls import path
from . import views

urlpatterns = [
    path('', views.news_main, name='news_main_page'),
    path('add/', views.add_entry, name='add_entry_page'),
    path('<int:pk>', views.NewsArticleDetail.as_view(), name='article_detail'),
    path('<int:pk>/edit', views.NewsArticleEdit.as_view(), name='article_edit'),
    path('<int:pk>/delete', views.NewsArticleDelete.as_view(), name='article_delete'),
]
