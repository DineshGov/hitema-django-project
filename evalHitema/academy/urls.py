from django.urls import path
from . import views

urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('sports/', views.show_sports, name='sports'),
    path('create/sport/', views.create_sport, name='create_sport'),
    path('read/sport/<int:id_sport>/', views.read_sport, name='read_sport'),
    path('update/sport/<int:id_sport>/', views.update_sport, name='update_sport'),
    path('delete/sport/<int:id_sport>/', views.delete_sport, name='delete_sport'),
    path('equipes/', views.show_equipes, name='equipes'),
    path('create/equipe/', views.create_equipe, name='create_equipe'),
    path('read/equipe/<int:id_equipe>/', views.read_equipe, name='read_equipe'),
    path('update/equipe/<int:id_equipe>/', views.update_equipe, name='update_equipe'),
    path('delete/equipe/<int:id_equipe>/', views.delete_equipe, name='delete_equipe'),
    path('joueurs/', views.show_joueurs, name='joueurs'),
    path('create/joueur/', views.create_joueur, name='create_joueur'),
    path('read/joueur/<int:id_joueur>/', views.read_joueur, name='read_joueur'),
    path('update/joueur/<int:id_joueur>/', views.update_joueur, name='update_joueur'),
    path('delete/joueur/<int:id_joueur>/', views.delete_joueur, name='delete_joueur'),
]
