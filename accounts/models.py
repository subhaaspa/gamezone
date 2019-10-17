from django.db import models

# Create your models here.

class GameProgress(models.Model):
    game_id = models.CharField(max_length=10)
    game_type = models.CharField(max_length=10)
    game_state = models.CharField(max_length=255)
    game_user = models.CharField(max_length=100)

    def __str__():
        return   "{}:{}".format(game_type, game_id)


    def save_game(self, game_id,game_type,game_state,game_user):
        self.game_id = game_id
        self.game_type = game_type
        self.game_state = game_state
        self.game_user = game_user
        super().save()
