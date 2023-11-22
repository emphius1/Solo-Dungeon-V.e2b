from django.test import TestCase
from game.models import CharacterModel, InventoryModel, CombatModel, QuestModel, MapModel, JournalModel, BestiaryModel, NPCRelationshipModel
from game.engine import GameEngine
from game.llm_integration import LLMIntegration
from game.content_management import ContentManagement
from game.ai_dungeon_master import AIDungeonMaster

class CharacterModelTestCase(TestCase):
    def setUp(self):
        CharacterModel.objects.create(name="Test Character", level=1, race="Human", character_class="Warrior")

    def test_character_creation(self):
        test_character = CharacterModel.objects.get(name="Test Character")
        self.assertEqual(test_character.level, 1)
        self.assertEqual(test_character.race, "Human")
        self.assertEqual(test_character.character_class, "Warrior")

class InventoryModelTestCase(TestCase):
    def setUp(self):
        InventoryModel.objects.create(character_id=1, item_name="Sword", quantity=1)

    def test_inventory_update(self):
        test_inventory = InventoryModel.objects.get(character_id=1)
        self.assertEqual(test_inventory.item_name, "Sword")
        self.assertEqual(test_inventory.quantity, 1)

class CombatModelTestCase(TestCase):
    def setUp(self):
        CombatModel.objects.create(character_id=1, enemy_name="Goblin", is_combat_active=True)

    def test_combat_state(self):
        test_combat = CombatModel.objects.get(character_id=1)
        self.assertTrue(test_combat.is_combat_active)
        self.assertEqual(test_combat.enemy_name, "Goblin")

class QuestModelTestCase(TestCase):
    def setUp(self):
        QuestModel.objects.create(character_id=1, quest_name="The Forgotten Treasure", is_quest_completed=False)

    def test_quest_log(self):
        test_quest = QuestModel.objects.get(character_id=1)
        self.assertFalse(test_quest.is_quest_completed)
        self.assertEqual(test_quest.quest_name, "The Forgotten Treasure")

class MapModelTestCase(TestCase):
    def setUp(self):
        MapModel.objects.create(character_id=1, map_name="The Dark Forest", has_been_explored=False)

    def test_map_change(self):
        test_map = MapModel.objects.get(character_id=1)
        self.assertFalse(test_map.has_been_explored)
        self.assertEqual(test_map.map_name, "The Dark Forest")

class JournalModelTestCase(TestCase):
    def setUp(self):
        JournalModel.objects.create(character_id=1, entry_text="Day 1: The journey begins.")

    def test_journal_entry(self):
        test_journal = JournalModel.objects.get(character_id=1)
        self.assertEqual(test_journal.entry_text, "Day 1: The journey begins.")

class BestiaryModelTestCase(TestCase):
    def setUp(self):
        BestiaryModel.objects.create(creature_name="Dragon", creature_description="A fearsome beast with fiery breath.")

    def test_bestiary_entry(self):
        test_bestiary = BestiaryModel.objects.get(creature_name="Dragon")
        self.assertEqual(test_bestiary.creature_description, "A fearsome beast with fiery breath.")

class NPCRelationshipModelTestCase(TestCase):
    def setUp(self):
        NPCRelationshipModel.objects.create(character_id=1, npc_name="Merlin", relationship_level=5)

    def test_npc_relationship_update(self):
        test_npc_relationship = NPCRelationshipModel.objects.get(character_id=1)
        self.assertEqual(test_npc_relationship.npc_name, "Merlin")
        self.assertEqual(test_npc_relationship.relationship_level, 5)

class GameEngineTestCase(TestCase):
    def test_game_state(self):
        engine = GameEngine()
        self.assertTrue(engine.check_game_state())

class LLMIntegrationTestCase(TestCase):
    def test_llm_response(self):
        llm = LLMIntegration()
        self.assertTrue(llm.get_response("Hello, Dungeon Master!"))

class ContentManagementTestCase(TestCase):
    def test_content_addition(self):
        content_manager = ContentManagement()
        self.assertTrue(content_manager.add_content("New Quest"))

class AIDungeonMasterTestCase(TestCase):
    def test_ai_conversation(self):
        ai_dm = AIDungeonMaster()
        self.assertTrue(ai_dm.converse_with_player("What will you do?"))