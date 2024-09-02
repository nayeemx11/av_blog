from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('post_list/', views.post_list, name="post_list"),
    path('post_detail_view/<int:id>/', views.post_detail_view, name="post_detail_view")
]
