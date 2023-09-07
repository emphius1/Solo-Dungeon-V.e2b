```python
import json
import os
from utils import error_handlers

DATA_DIR = "data"

def create_data_dir():
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)

def save_data(file_name, data):
    try:
        with open(os.path.join(DATA_DIR, file_name), 'w') as f:
            json.dump(data, f)
    except Exception as e:
        error_handlers.handle_error(e)

def load_data(file_name):
    try:
        with open(os.path.join(DATA_DIR, file_name), 'r') as f:
            return json.load(f)
    except Exception as e:
        error_handlers.handle_error(e)

def update_data(file_name, data):
    try:
        existing_data = load_data(file_name)
        existing_data.update(data)
        save_data(file_name, existing_data)
    except Exception as e:
        error_handlers.handle_error(e)

def delete_data(file_name):
    try:
        os.remove(os.path.join(DATA_DIR, file_name))
    except Exception as e:
        error_handlers.handle_error(e)
```