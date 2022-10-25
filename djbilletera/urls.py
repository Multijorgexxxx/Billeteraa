
from django.contrib import admin
from django.urls import path
from login import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    # LOGIN
    path('crear_cuenta/', views.signup, name='crear_cuenta'),
    path('login/', views.signin, name='login'),
    path('cerrar_sesion/', views.signout, name='signout'),
]
