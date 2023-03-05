# I should work on complex dict structure, need a simple method to get data

# Example
# dict_nested_key_getter(data, ['first_level_key', 'second_level_key'])

def dict_nested_key_getter(instance: dict, keys: list):
    for key in keys:
        if instance:
            instance = instance.get(key, {})
    return instance
