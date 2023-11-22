from django.contrib import admin
from .models import CharacterModel, InventoryModel, CombatModel, QuestModel, MapModel, JournalModel, BestiaryModel, NPCRelationshipModel, GameStateModel, PlayerProgressModel, EventModel, AIResponseModel

class CharacterModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'race', 'character_class', 'level']

class InventoryModelAdmin(admin.ModelAdmin):
    list_display = ['character', 'item_name', 'quantity']

class CombatModelAdmin(admin.ModelAdmin):
    list_display = ['character', 'enemy', 'combat_type']

class QuestModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'status']

class MapModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']

class JournalModelAdmin(admin.ModelAdmin):
    list_display = ['entry_date', 'content']

class BestiaryModelAdmin(admin.ModelAdmin):
    list_display = ['creature_name', 'creature_type', 'challenge_rating']

class NPCRelationshipModelAdmin(admin.ModelAdmin):
    list_display = ['character', 'npc_name', 'relationship_level']

class GameStateModelAdmin(admin.ModelAdmin):
    list_display = ['state_name', 'value']

class PlayerProgressModelAdmin(admin.ModelAdmin):
    list_display = ['player', 'progress_metric', 'value']

class EventModelAdmin(admin.ModelAdmin):
    list_display = ['event_name', 'trigger_condition']

class AIResponseModelAdmin(admin.ModelAdmin):
    list_display = ['input', 'response']

admin.site.register(CharacterModel, CharacterModelAdmin)
admin.site.register(InventoryModel, InventoryModelAdmin)
admin.site.register(CombatModel, CombatModelAdmin)
admin.site.register(QuestModel, QuestModelAdmin)
admin.site.register(MapModel, MapModelAdmin)
admin.site.register(JournalModel, JournalModelAdmin)
admin.site.register(BestiaryModel, BestiaryModelAdmin)
admin.site.register(NPCRelationshipModel, NPCRelationshipModelAdmin)
admin.site.register(GameStateModel, GameStateModelAdmin)
admin.site.register(PlayerProgressModel, PlayerProgressModelAdmin)
admin.site.register(EventModel, EventModelAdmin)
admin.site.register(AIResponseModel, AIResponseModelAdmin)