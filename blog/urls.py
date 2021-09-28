# blog/urls.py

from django.urls import path
from .views import BlogListView
from .views import BlogDetailView  # new

# from django.contrib.staticfiles.urls import staticfiles_urlpatterns  # stackoverflow

urlpatterns = [
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
    path('', BlogListView.as_view(), name='home')
]

# urlpatterns += staticfiles_urlpatterns()  # stackoverflow
