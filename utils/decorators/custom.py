# Need a custom decorator to handle different data based on decorated function
# Decorator params stored in kwargs
# @custom_decorator(param=1, other_param='xyz', last_param=EnumClass.CHOICE, why_not_another_param='yeah why not')

from functools import wraps
from typing import Callable

get_function_path: Callable[[str, str], str] = lambda filename, prefix, name: f'{filename.replace(prefix, "").replace(".py", "").replace("/", ".")}.{name}'

def custom_decorator(*args, **kwargs):
    def decorator(function):
        # Get nested function
        while '__wrapped__' in function.__dict__:
            function = function.__dict__.get('__wrapped__')

        try:
            function_path = get_function_path(function.__code__.co_filename, function.__name__)

            # Decorator params stored in kwargs
            # Do stuff            
        except:
            # Log errors
            pass

        @wraps(function)
        def wrapper(*args, **kwargs):
            return function(*args)
        return wrapper
    return decorator
