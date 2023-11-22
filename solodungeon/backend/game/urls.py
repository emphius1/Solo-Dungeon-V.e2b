from django.urls import path
from . import views

urlpatterns = [
    path('character/create/', views.createCharacter, name='create-character'),
    path('character/manage/', views.manageCharacter, name='manage-character'),
    path('inventory/', views.updateInventory, name='update-inventory'),
    path('combat/', views.executeCombat, name='execute-combat'),
    path('quest/', views.logQuest, name='log-quest'),
    path('map/', views.updateMap, name='update-map'),
    path('journal/', views.addJournalEntry, name='add-journal-entry'),
    path('bestiary/', views.addBestiaryEntry, name='add-bestiary-entry'),
    path('npc-relationships/', views.updateNPCRelationship, name='update-npc-relationship'),
    path('game-state/save/', views.saveGameState, name='save-game-state'),
    path('player-progress/', views.updatePlayerProgress, name='update-player-progress'),
    path('event/trigger/', views.triggerEvent, name='trigger-event'),
    path('ai/response/', views.getAIResponse, name='get-ai-response'),
]