from django.urls import path
from . import views

from .views import HomeView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserHomeView

urlpatterns=[
    path('', HomeView.as_view(), name='blog-home'),
    path('user/<str:username>/', UserHomeView.as_view(), name='user-blog-home'),
    path('post/<int:pk>/',PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update',PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete',PostDeleteView.as_view(), name='post-delete'),
    path('post/new/',PostCreateView.as_view(), name='create-post'),
    path('about/',views.about, name='blog-about'),
    path('contact/',views.contact, name='blog-contact'),
    path('hello/',views.hello)
]