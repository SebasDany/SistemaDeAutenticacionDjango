from django.urls import path,re_path
from bases.views import Home
from django.contrib.auth import views as auth_views
from django.views.static import serve
from django.conf import settings

from .views import validar,valid,registrarPersona


urlpatterns = [
   path('',Home.as_view(),name='home'),
   path('registrarPersona',registrarPersona, name="rP"),
   # path('',home,name='home'),
   path('login/',auth_views.LoginView.as_view(template_name='bases/login.html'),name='login'),
   path('logout/',auth_views.LogoutView.as_view(template_name='bases/login.html'),name='logout'),
   #path('validar/',auth_views.LoginView.as_view(template_name='bases/autenticar.html'),name='val'),
   path('validar/',validar,name='val'),
   # path('success/',success,name='vall'),
   path('valid/<str:name>/',valid,name='scs'),


  
]


urlpatterns +=[
   re_path(r'^media/(?P<path>.*)$',serve,{'document_root':settings.MEDIA_ROOT})

] 