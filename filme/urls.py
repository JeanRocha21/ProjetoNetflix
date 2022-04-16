from django.urls import path, reverse_lazy
from .views import Homefilmes, Detalhesfilmes, pesquisafilmes, editarperfil, criarconta, Homepage
from django.contrib.auth import views as auth_views

app_name = 'filme'


urlpatterns = [
    path('', Homepage.as_view(), name='Homepage'),
    path('filmes/', Homefilmes.as_view(), name='Homefilmes'),
    path('filmes/<int:pk>', Detalhesfilmes.as_view(), name='Detalhesfilmes'),
    path('pesquisafilmes/', pesquisafilmes.as_view(), name='pesquisafilmes'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('editarperfil/<int:pk>', editarperfil.as_view(), name='editarperfil'),
    path('criarconta/', criarconta.as_view(), name='criarconta'),
    path('mudarsenha/', auth_views.PasswordChangeView.as_view(template_name='editarperfil.html',
                                                               success_url=reverse_lazy("filme:Homefilmes")), name='mudarsenha'),

]


