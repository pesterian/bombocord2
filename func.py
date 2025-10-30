import json
from typing import Optional


def load_json(filepath: str) -> dict:
    """Load JSON file and return as dictionary."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        return {}


def save_json(filepath: str, data: dict) -> bool:
    """Save dictionary to JSON file."""
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        return True
    except Exception as e:
        print(f"Error saving JSON: {e}")
        return False


def get_dict_entry(key: str, filepath: str) -> Optional[str]:
    """Get a value from the dictionary by key."""
    data = load_json(filepath)
    return data.get(key.lower())


def get_all_keys(filepath: str) -> list:
    """Get all keys from the dictionary in alphabetical order."""
    data = load_json(filepath)
    return sorted(data.keys())


def add_dict_entry(key: str, value: str, filepath: str) -> tuple[bool, str]:
    """
    Add a new entry to the dictionary.
    Returns (success, message).
    """
    data = load_json(filepath)
    key_lower = key.lower()
    
    if key_lower in data:
        return False, f"Key '{key}' already exists!"
    
    data[key_lower] = value
    if save_json(filepath, data):
        return True, f"Successfully added '{key}'"
    return False, "Error saving file"


def remove_dict_entry(key: str, filepath: str) -> tuple[bool, str]:
    """
    Remove an entry from the dictionary.
    Returns (success, message).
    """
    data = load_json(filepath)
    key_lower = key.lower()
    
    if key_lower not in data:
        return False, f"Key '{key}' doesn't exist!"
    
    del data[key_lower]
    if save_json(filepath, data):
        return True, f"Successfully removed '{key}'"
    return False, "Error saving file"


def update_dict_entry(key: str, new_value: str, filepath: str) -> tuple[bool, str]:
    """
    Update an existing entry in the dictionary.
    Returns (success, message).
    """
    data = load_json(filepath)
    key_lower = key.lower()
    
    if key_lower not in data:
        return False, f"Key '{key}' doesn't exist!"
    
    data[key_lower] = new_value
    if save_json(filepath, data):
        return True, f"Successfully updated '{key}'"
    return False, "Error saving file"


def is_admin(user_id: int, filepath: str) -> bool:
    """Check if a user ID is in the admins list."""
    admins = load_json(filepath)
    return str(user_id) in admins and admins[str(user_id)] is True


def get_random_entry(filepath: str) -> Optional[tuple[str, str]]:
    """Get a random key-value pair from the dictionary."""
    import random
    data = load_json(filepath)
    
    if not data:
        return None
    
    key = random.choice(list(data.keys()))
    return (key, data[key])
