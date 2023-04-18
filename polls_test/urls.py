from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('employee',views.emp_result, name ='result'),
    path('member',views.display, name='display'),
    path('groups',views.display_group,name='display_group'),
    path('user',views.display_join, name='user'),
    path('<str:user_id>/user_reg',views.user_reg, name='user_reg'),
    #path('<str:user_id>/userView',views.userView, name='user_view'),
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)