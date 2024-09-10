from django.urls import path
from . import views

app_name = 'shop'
urlpatterns = [
    path('', views.painting_list, name='painting_list'),
    path('<slug:tag_slug>/', views.painting_list,
         name='painting_list_by_tag'),
    path('<int:id>/<slug:slug>/', views.painting_detail,
         name='painting_detail'),
]
