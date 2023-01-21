import json
import functools

def to_json(func):
    @functools.wraps(func)
    def wrapped(*args, **kwargs) -> str:
        result = func(*args, **kwargs)
        data = json.dumps(result)
        return data
    return wrapped
