import contextlib
import logging
from datetime import datetime
from functools import wraps


@contextlib.contextmanager
def time_tracker(name):
    """Time a block of code in a very simple way with logging statements."""
    start = datetime.now()
    yield
    finish = datetime.now()
    elapsed = (finish - start).total_seconds()
    print('PROFILER - %s - %f seconds' % (name, elapsed))


def time_tracked(func, extra=None):
    """The wrapped function outputs its own execution time.

    The result is attached to the function's name.
    """
    if isinstance(func, str):
        # Something is using the decorator as a decorator decorator.
        return lambda _func: time_tracked(func=_func, extra=func)

    @wraps(func)
    def wrapped(*args, **kwargs):
        with time_tracker(name=func.__name__, extra=extra):
            return func(*args, **kwargs)

    return wrapped
