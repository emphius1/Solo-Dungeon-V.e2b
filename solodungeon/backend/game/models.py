from django.db import models

class CharacterModel(models.Model):
    name = models.CharField(max_length=100)
    race = models.CharField(max_length=50)
    character_class = models.CharField(max_length=50)
    level = models.IntegerField(default=1)
    experience = models.IntegerField(default=0)
    strength = models.IntegerField()
    dexterity = models.IntegerField()
    constitution = models.IntegerField()
    intelligence = models.IntegerField()
    wisdom = models.IntegerField()
    charisma = models.IntegerField()
    hit_points = models.IntegerField()
    max_hit_points = models.IntegerField()
    inventory = models.JSONField()
    quests = models.JSONField()
    map_position = models.JSONField()
    journal_entries = models.JSONField()

    def __str__(self):
        return self.name

class InventoryModel(models.Model):
    character = models.ForeignKey(CharacterModel, on_delete=models.CASCADE, related_name='character_inventory')
    items = models.JSONField()

    def __str__(self):
        return f"{self.character.name}'s Inventory"

class CombatModel(models.Model):
    character = models.ForeignKey(CharacterModel, on_delete=models.CASCADE, related_name='character_combat')
    combat_log = models.TextField()

    def __str__(self):
        return f"{self.character.name}'s Combat Log"

class QuestModel(models.Model):
    character = models.ForeignKey(CharacterModel, on_delete=models.CASCADE, related_name='character_quests')
    title = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(max_length=50)
    objectives = models.JSONField()

    def __str__(self):
        return self.title

class MapModel(models.Model):
    character = models.ForeignKey(CharacterModel, on_delete=models.CASCADE, related_name='character_map')
    map_data = models.JSONField()

    def __str__(self):
        return f"{self.character.name}'s Map"

class JournalModel(models.Model):
    character = models.ForeignKey(CharacterModel, on_delete=models.CASCADE, related_name='character_journal')
    entry = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Journal Entry {self.id}"

class BestiaryModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    stats = models.JSONField()

    def __str__(self):
        return self.name

class NPCRelationshipModel(models.Model):
    character = models.ForeignKey(CharacterModel, on_delete=models.CASCADE, related_name='character_npc_relationships')
    npc_name = models.CharField(max_length=100)
    relationship_level = models.IntegerField()
    interactions = models.JSONField()

    def __str__(self):
        return f"{self.character.name}'s Relationship with {self.npc_name}"

class GameStateModel(models.Model):
    character = models.OneToOneField(CharacterModel, on_delete=models.CASCADE, related_name='character_game_state')
    state_data = models.JSONField()

    def __str__(self):
        return f"{self.character.name}'s Game State"

class PlayerProgressModel(models.Model):
    character = models.OneToOneField(CharacterModel, on_delete=models.CASCADE, related_name='character_progress')
    progress_data = models.JSONField()

    def __str__(self):
        return f"{self.character.name}'s Progress"

class EventModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    trigger_conditions = models.JSONField()

    def __str__(self):
        return self.name

class AIResponseModel(models.Model):
    input_data = models.JSONField()
    response = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"AI Response {self.id}"