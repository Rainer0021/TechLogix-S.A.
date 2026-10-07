from django.urls import path
from . import views
from django.contrib.auth.views import LoginView
from .views import CustomLoginView
urlpatterns = [
    path('', views.index, name='index'),
    path('catalogo/', views.catalogo, name='catalogo'),
    path('admin_panel/', views.admin_panel, name='admin_panel'),
    path('admin_panel/crear/', views.producto_crear, name='producto_crear'),
    path('admin_panel/editar/<int:pk>/', views.producto_editar, name='producto_editar'),
    path('admin_panel/eliminar/<int:pk>/', views.producto_eliminar, name='producto_eliminar'),
    path('accounts/login/', CustomLoginView.as_view(template_name='login.html'), name='login'),
]