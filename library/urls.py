from django.urls import path

from . import views

app_name = 'library'
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('alg/<int:pk>/', views.AlgView.as_view(), name='alg'),
    path('categories', views.CategoriesView.as_view(), name='categories'),
]
