from django.db import models
from .models import CharacterModel, InventoryModel, CombatModel, QuestModel, MapModel, JournalModel, BestiaryModel, NPCRelationshipModel

class ContentManager:
    def __init__(self):
        # Initialize any necessary properties here
        pass

    def add_character(self, character_data):
        character = CharacterModel(**character_data)
        character.save()
        return character

    def update_inventory(self, character_id, inventory_data):
        character = CharacterModel.objects.get(id=character_id)
        character.inventory.update_or_create(defaults=inventory_data)
        character.save()
        return character.inventory

    def record_combat_event(self, combat_data):
        combat_event = CombatModel(**combat_data)
        combat_event.save()
        return combat_event

    def add_quest(self, quest_data):
        quest = QuestModel(**quest_data)
        quest.save()
        return quest

    def update_map(self, map_data):
        map_instance = MapModel(**map_data)
        map_instance.save()
        return map_instance

    def add_journal_entry(self, journal_data):
        journal_entry = JournalModel(**journal_data)
        journal_entry.save()
        return journal_entry

    def add_bestiary_entry(self, bestiary_data):
        bestiary_entry = BestiaryModel(**bestiary_data)
        bestiary_entry.save()
        return bestiary_entry

    def update_npc_relationships(self, npc_id, relationship_data):
        npc_relationship = NPCRelationshipModel.objects.get(npc_id=npc_id)
        npc_relationship.update(**relationship_data)
        npc_relationship.save()
        return npc_relationship

    # Additional methods for content management can be added here

# This module can be expanded with more complex content management logic as needed.