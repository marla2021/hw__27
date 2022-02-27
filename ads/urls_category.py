from django.contrib import admin
from django.urls import path

from ads import views
from ads.views import category

urlpatterns = [
    path('', category.CategoryListView.as_view()),
    path('create/', category.CategoryCreateView.as_view()),
    path('<int:pk>', category.CategoryDetailView.as_view()),
    path('<int:pk>/update/', category.CategoryUpdateView.as_view()),
    path('<int:pk>/delete/', category.CategoryDeleteView.as_view()),
]
