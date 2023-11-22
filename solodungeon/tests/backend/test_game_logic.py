from django.test import TestCase
from game.models import CharacterModel, GameStateModel
from game.engine import GameEngine

class GameLogicTests(TestCase):
    def setUp(self):
        # Setup initial game state and character
        self.character = CharacterModel.objects.create(
            name="Test Character",
            level=1,
            race="Human",
            character_class="Warrior",
            hit_points=10,
            experience=0
        )
        self.game_state = GameStateModel.objects.create(
            current_location="Starting Village",
            world_time=0,
            character=self.character
        )
        self.engine = GameEngine()

    def test_character_creation(self):
        # Test character creation logic
        self.assertEqual(self.character.name, "Test Character")
        self.assertEqual(self.character.level, 1)
        self.assertEqual(self.character.race, "Human")
        self.assertEqual(self.character.character_class, "Warrior")
        self.assertEqual(self.character.hit_points, 10)
        self.assertEqual(self.character.experience, 0)

    def test_game_state_initialization(self):
        # Test initial game state
        self.assertEqual(self.game_state.current_location, "Starting Village")
        self.assertEqual(self.game_state.world_time, 0)
        self.assertEqual(self.game_state.character, self.character)

    def test_game_progression(self):
        # Test game progression logic
        self.engine.advance_time(self.game_state, 5)
        self.assertEqual(self.game_state.world_time, 5)

        self.engine.gain_experience(self.character, 50)
        self.assertEqual(self.character.experience, 50)

    def test_combat_mechanics(self):
        # Test combat mechanics
        enemy_hp = 5
        damage_dealt = self.engine.calculate_damage(self.character, enemy_hp)
        enemy_hp -= damage_dealt
        self.assertTrue(enemy_hp <= 0, "Enemy should be defeated")

    def test_quest_completion(self):
        # Test quest completion logic
        quest_reward = 100
        self.engine.complete_quest(self.character, quest_reward)
        self.assertEqual(self.character.experience, quest_reward)

    def test_save_game_state(self):
        # Test saving game state
        self.game_state.current_location = "Dungeon Entrance"
        self.game_state.save()
        updated_state = GameStateModel.objects.get(id=self.game_state.id)
        self.assertEqual(updated_state.current_location, "Dungeon Entrance")