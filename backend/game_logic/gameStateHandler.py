```python
import json
from backend.database.models.characterModel import Character
from backend.database.models.gameHistoryModel import GameHistory
from backend.database.models.campaignSettingsModel import CampaignSettings

class GameStateHandler:
    def __init__(self, db_adapter):
        self.db_adapter = db_adapter

    def load_game_state(self, player_id):
        """
        Load the game state for a given player from the database.
        """
        character_data = self.db_adapter.fetch_character_data(player_id)
        game_history_data = self.db_adapter.fetch_game_history(player_id)
        campaign_settings_data = self.db_adapter.fetch_campaign_settings(player_id)

        character = Character(**character_data)
        game_history = GameHistory(**game_history_data)
        campaign_settings = CampaignSettings(**campaign_settings_data)

        return {
            'character': character,
            'game_history': game_history,
            'campaign_settings': campaign_settings
        }

    def save_game_state(self, player_id, character, game_history, campaign_settings):
        """
        Save the current game state for a given player to the database.
        """
        character_data = character.to_dict()
        game_history_data = game_history.to_dict()
        campaign_settings_data = campaign_settings.to_dict()

        self.db_adapter.update_character_data(player_id, character_data)
        self.db_adapter.update_game_history(player_id, game_history_data)
        self.db_adapter.update_campaign_settings(player_id, campaign_settings_data)

    def reset_game_state(self, player_id):
        """
        Reset the game state for a given player in the database.
        """
        self.db_adapter.reset_character_data(player_id)
        self.db_adapter.reset_game_history(player_id)
        self.db_adapter.reset_campaign_settings(player_id)

# Example usage:
# db_adapter = createDatabaseAdapter('postgresql') # or 'mongodb'
# game_state_handler = GameStateHandler(db_adapter)
# player_id = 'player123'
# game_state = game_state_handler.load_game_state(player_id)
# game_state_handler.save_game_state(player_id, game_state['character'], game_state['game_history'], game_state['campaign_settings'])
```