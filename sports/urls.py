from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create-match', views.create_match, name='match_form'),
    path('matches', views.all_matches, name='all_matches'),
    path('matches/<int:id>', views.match_detail, name='match-detail'),
    path('match-created', views.match_created)
]
