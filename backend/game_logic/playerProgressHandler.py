```python
from django.db import models
from .models.characterModel import Character
from .models.gameHistoryModel import GameHistory

class PlayerProgressHandler:
    def __init__(self):
        # Initialize any required variables or services here
        pass

    def update_player_progress(self, character_id, progress_data):
        """
        Update the player's progress in the game, including experience points, level, and quest status.
        """
        try:
            character = Character.objects.get(id=character_id)
            character.experience += progress_data.get('experience', 0)
            character.level = progress_data.get('level', character.level)
            character.save()

            # Log the progress update in the game history
            GameHistory.objects.create(character=character, description="Player progress updated.")

            return True, "Player progress updated successfully."
        except Character.DoesNotExist:
            return False, "Character not found."
        except Exception as e:
            return False, str(e)

    def get_player_progress(self, character_id):
        """
        Retrieve the player's current progress, including experience points, level, and quest status.
        """
        try:
            character = Character.objects.get(id=character_id)
            progress_data = {
                'experience': character.experience,
                'level': character.level,
                'quests': character.quests.all()  # Assuming a related name 'quests' for quest model
            }
            return True, progress_data
        except Character.DoesNotExist:
            return False, "Character not found."
        except Exception as e:
            return False, str(e)

    def reset_player_progress(self, character_id):
        """
        Reset the player's progress, typically used when starting a new game or after a character's demise.
        """
        try:
            character = Character.objects.get(id=character_id)
            character.experience = 0
            character.level = 1
            character.quests.clear()  # Assuming a ManyToMany relationship with quests
            character.save()

            # Log the progress reset in the game history
            GameHistory.objects.create(character=character, description="Player progress reset.")

            return True, "Player progress reset successfully."
        except Character.DoesNotExist:
            return False, "Character not found."
        except Exception as e:
            return False, str(e)
```