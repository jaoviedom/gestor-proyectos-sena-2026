from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
  path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
  path('logout/', auth_views.LogoutView.as_view(), name='logout'),
  path('registro/', views.registro, name='registro'),
  path('grupos/', views.grupos, name='grupos'),
  path('grupos/<int:id_grupo>/editar/', views.editar_grupo, name='editar_grupo'),
  path('grupos/<int:id_grupo>/eliminar/', views.eliminar_grupo, name='eliminar_grupo'),
  path('grupos/<int:id_grupo>/agregar-usuario/', views.agregar_usuario_grupo, name='agregar_usuario_grupo'),
  path('grupos/<int:id_grupo>/eliminar-usuario/', views.eliminar_usuario_grupo, name='eliminar_usuario_grupo'),
]