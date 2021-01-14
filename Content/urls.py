from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('blog/<str:slug>/', views.BlogSingle.as_view(), name='blog_single'),
]
