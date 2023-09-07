```python
import sqlite3

def initialize_db():
    conn = sqlite3.connect('game_data.db')
    c = conn.cursor()

    # Create table for characters
    c.execute('''
        CREATE TABLE characters (
            id INTEGER PRIMARY KEY,
            name TEXT,
            class TEXT,
            level INTEGER,
            stats TEXT,
            inventory TEXT
        )
    ''')

    # Create table for quests
    c.execute('''
        CREATE TABLE quests (
            id INTEGER PRIMARY KEY,
            name TEXT,
            description TEXT,
            status TEXT,
            reward TEXT,
            origin TEXT
        )
    ''')

    # Create table for AI-generated content
    c.execute('''
        CREATE TABLE ai_content (
            id INTEGER PRIMARY KEY,
            content_type TEXT,
            content TEXT,
            context TEXT
        )
    ''')

    # Create table for player saves
    c.execute('''
        CREATE TABLE player_saves (
            id INTEGER PRIMARY KEY,
            character_id INTEGER,
            quest_id INTEGER,
            game_state TEXT,
            FOREIGN KEY(character_id) REFERENCES characters(id),
            FOREIGN KEY(quest_id) REFERENCES quests(id)
        )
    ''')

    # Save (commit) the changes and close the connection
    conn.commit()
    conn.close()

if __name__ == "__main__":
    initialize_db()
```