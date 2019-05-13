def inspect(func):
    def wrapped_func(*args, **kwargs):
        print(f"Running {func.__name__}")
        val = func(*args)
        print(val)
        return val
    return wrapped_func

@inspect
def combine(a, b):
    return a + b

