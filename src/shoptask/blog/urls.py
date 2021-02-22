from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    #path('<slug:slug>/', views.PostDetail.as_view(),name='post_detail'),
    path('blog/<slug:slug>/', views.postDetail,name='post_detail'),
    path('register/', views.registerPage, name='register')
]