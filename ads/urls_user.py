from django.urls import path

from ads import views

urlpatterns = [
    path('', views.UserListView.as_view()),
    path('create/', views.UserCreateView.as_view()),
    # path('<int:pk>', views.CategoryDetailView.as_view()),
    # path('<int:pk>/update/', views.CategoryUpdateView.as_view()),
    # path('<int:pk>/delete/', views.CategoryDeleteView.as_view()),
]