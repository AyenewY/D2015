from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('member',views.display, name='display'),
    path('groups',views.display_group,name='display_group'),
    path('user',views.display_join, name='user'),
    path('user_reg',views.userView.as_view())
]