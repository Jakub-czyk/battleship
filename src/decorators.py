import functools
import logging

logging.basicConfig(filename='battleship.log', level=logging.INFO,
                    format='%(asctime)s %(levelname)s:%(message)s')

def log_action(func):
    """Dekorator logujący wywołania funkcji."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        logging.info(f"Called {func.__name__} with {args[1:] if len(args)>1 else ''} {kwargs}")
        result = func(*args, **kwargs)
        logging.info(f"{func.__name__} returned {result}")
        return result
    return wrapper
