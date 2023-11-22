from pymongo import MongoClient
from pymongo.collection import Collection
from backend.database.models.characterModel import CharacterSchema
from backend.database.models.gameHistoryModel import GameHistorySchema
from backend.database.models.campaignSettingsModel import CampaignSettingsSchema

class MongoDBAdapter:
    def __init__(self, uri: str, db_name: str):
        self.client = MongoClient(uri)
        self.db = self.client[db_name]
        self.character_collection: Collection = self.db['characters']
        self.game_history_collection: Collection = self.db['game_history']
        self.campaign_settings_collection: Collection = self.db['campaign_settings']

    def create_character(self, character_data: dict):
        if not CharacterSchema.validate(character_data):
            raise ValueError("Invalid character data")
        return self.character_collection.insert_one(character_data).inserted_id

    def update_character(self, character_id: str, character_data: dict):
        if not CharacterSchema.validate(character_data):
            raise ValueError("Invalid character data")
        return self.character_collection.update_one({'_id': character_id}, {'$set': character_data})

    def get_character(self, character_id: str):
        return self.character_collection.find_one({'_id': character_id})

    def delete_character(self, character_id: str):
        return self.character_collection.delete_one({'_id': character_id})

    def log_game_history(self, history_data: dict):
        if not GameHistorySchema.validate(history_data):
            raise ValueError("Invalid game history data")
        return self.game_history_collection.insert_one(history_data).inserted_id

    def update_campaign_settings(self, settings_id: str, settings_data: dict):
        if not CampaignSettingsSchema.validate(settings_data):
            raise ValueError("Invalid campaign settings data")
        return self.campaign_settings_collection.update_one({'_id': settings_id}, {'$set': settings_data})

    def get_campaign_settings(self, settings_id: str):
        return self.campaign_settings_collection.find_one({'_id': settings_id})

    def create_campaign_settings(self, settings_data: dict):
        if not CampaignSettingsSchema.validate(settings_data):
            raise ValueError("Invalid campaign settings data")
        return self.campaign_settings_collection.insert_one(settings_data).inserted_id

# Example usage:
# adapter = MongoDBAdapter(uri="mongodb://localhost:27017", db_name="dnd_game")
# character_id = adapter.create_character(character_data)
# adapter.update_character(character_id, updated_character_data)
# character = adapter.get_character(character_id)
# adapter.delete_character(character_id)
# game_history_id = adapter.log_game_history(history_data)
# campaign_settings_id = adapter.create_campaign_settings(settings_data)
# adapter.update_campaign_settings(campaign_settings_id, updated_settings_data)
# settings = adapter.get_campaign_settings(campaign_settings_id)