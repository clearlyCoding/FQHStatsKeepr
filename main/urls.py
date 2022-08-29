from django.urls import path
from .views import GameView

# from . import views



app_name = 'main' #namespace



urlpatterns = [
	path  ('home', GameView.as_view())
]


# urlpatterns = [
# 	path ("", views.homepage, name = "homepage"),
# 	path ("newGame/", views.newGame, name = "newGame"),
# 	path ("gamePlay/", views.gamePlay, name = "gamePlay"),
# 	path ("endgame/", views.endgame, name = "endgame"),
# ]