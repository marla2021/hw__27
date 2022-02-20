from django.contrib import admin
from django.urls import path

from ads import views

urlpatterns = [
    path('/', views.CategoryListView.as_view()),
    path('create/', views.CategoryCreateView.as_view()),
    path('<int:pk>', views.CategoryDetailView.as_view()),
    path('<int:pk>/update/', views.CategoryUpdateViev.as_view()),
    path('<int:pk>/delete/', views.CategoryDeleteViev.as_view()),

    path('ad/', views.AdView.as_view()),
    path('ad/<int:pk>', views.AdDetailView.as_view()),
]
