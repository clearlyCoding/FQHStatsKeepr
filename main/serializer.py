from rest_framework import serializers
from .models import Game

class GameDisplay(serializers.ModelSerializer):
	class Meta:
		model = Game
		fields = ('teamRed_score','teamBlue_score',	'teamRed_players',	'teamBlue_players',	
			'teamRed_indexPlayerGoalsandAssist', 'teamBlue_indexPlayerGoalsandAssist',	'game_Complete', 'game_Date',	'game_code')