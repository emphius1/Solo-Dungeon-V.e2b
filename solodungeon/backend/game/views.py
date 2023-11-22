from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from .models import CharacterModel, InventoryModel, CombatModel, QuestModel, MapModel, JournalModel, BestiaryModel, NPCRelationshipModel
from .engine import saveGameState, updatePlayerProgress
from .llm_integration import getAIResponse
from .ai_dungeon_master import AIResponseReceived

@require_http_methods(["POST"])
def create_character(request):
    # Assuming JSON data with character details is sent in the request
    data = request.POST
    character = CharacterModel.objects.create(**data)
    return JsonResponse({'message': 'CharacterCreated', 'character_id': character.id}, status=201)

@require_http_methods(["GET", "POST", "PUT", "DELETE"])
def manage_character(request, character_id):
    if request.method == 'GET':
        character = CharacterModel.objects.get(id=character_id)
        return JsonResponse(character.to_dict(), safe=False)
    elif request.method == 'POST':
        data = request.POST
        character, created = CharacterModel.objects.update_or_create(id=character_id, defaults=data)
        if created:
            return JsonResponse({'message': 'CharacterCreated', 'character_id': character.id}, status=201)
        else:
            return JsonResponse({'message': 'CharacterUpdated', 'character_id': character.id}, status=200)
    elif request.method == 'PUT':
        data = request.PUT
        CharacterModel.objects.filter(id=character_id).update(**data)
        return JsonResponse({'message': 'CharacterUpdated', 'character_id': character_id}, status=200)
    elif request.method == 'DELETE':
        CharacterModel.objects.filter(id=character_id).delete()
        return JsonResponse({'message': 'CharacterDeleted', 'character_id': character_id}, status=200)

@require_http_methods(["GET"])
def get_inventory(request, character_id):
    inventory = InventoryModel.objects.filter(character_id=character_id)
    return JsonResponse(list(inventory.values()), safe=False)

@require_http_methods(["POST"])
def update_inventory(request, character_id):
    data = request.POST
    InventoryModel.objects.filter(character_id=character_id).update(**data)
    return JsonResponse({'message': 'InventoryUpdated', 'character_id': character_id}, status=200)

@require_http_methods(["POST"])
def execute_combat(request):
    data = request.POST
    combat_result = CombatModel.objects.create(**data)
    return JsonResponse({'message': 'CombatAction', 'combat_id': combat_result.id}, status=201)

@require_http_methods(["POST"])
def log_quest(request, character_id):
    data = request.POST
    quest = QuestModel.objects.create(character_id=character_id, **data)
    return JsonResponse({'message': 'QuestUpdated', 'quest_id': quest.id}, status=201)

@require_http_methods(["POST"])
def update_map(request):
    data = request.POST
    map_data = MapModel.objects.create(**data)
    return JsonResponse({'message': 'MapChanged', 'map_id': map_data.id}, status=201)

@require_http_methods(["POST"])
def add_journal_entry(request, character_id):
    data = request.POST
    journal_entry = JournalModel.objects.create(character_id=character_id, **data)
    return JsonResponse({'message': 'JournalEntryAdded', 'entry_id': journal_entry.id}, status=201)

@require_http_methods(["POST"])
def add_bestiary_entry(request):
    data = request.POST
    bestiary_entry = BestiaryModel.objects.create(**data)
    return JsonResponse({'message': 'BestiaryEntryAdded', 'entry_id': bestiary_entry.id}, status=201)

@require_http_methods(["POST"])
def update_npc_relationship(request, character_id):
    data = request.POST
    npc_relationship = NPCRelationshipModel.objects.create(character_id=character_id, **data)
    return JsonResponse({'message': 'NPCRelationshipUpdated', 'relationship_id': npc_relationship.id}, status=201)

@require_http_methods(["GET"])
def get_ai_response(request, character_id):
    data = request.GET
    response = getAIResponse(character_id, data)
    return JsonResponse({'message': AIResponseReceived, 'response': response}, status=200)