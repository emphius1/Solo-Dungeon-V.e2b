```python
import os
import json
from database import db_ops

def save_game(player, game_state):
    """
    Save the current game state to a JSON file.
    """
    save_data = {
        'player': player.to_dict(),
        'game_state': game_state
    }

    save_file = os.path.join('saves', f'{player.name}.json')

    with open(save_file, 'w') as f:
        json.dump(save_data, f)

    print(f"Game saved to {save_file}.")


def load_game(player_name):
    """
    Load a game state from a JSON file.
    """
    save_file = os.path.join('saves', f'{player_name}.json')

    if not os.path.exists(save_file):
        print(f"No save file found for player {player_name}.")
        return None, None

    with open(save_file, 'r') as f:
        save_data = json.load(f)

    player = db_ops.load_player_from_dict(save_data['player'])
    game_state = save_data['game_state']

    print(f"Game loaded from {save_file}.")

    return player, game_state
```