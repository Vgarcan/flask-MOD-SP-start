'''
Using `functools.wraps` in Python Decorators

`functools.wraps` is used to preserve the metadata of the original function when creating decorators. It maintains the original function’s name, docstring, and other attributes.

Example:
import functools

def my_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("Before func()")
        result = func(*args, **kwargs)
        print("After func()")
        return result
    return wrapper

@my_decorator
def say_hello(name):
    print(f"Hello, {name}!")

say_hello("World")


Without `functools.wraps`, the metadata of the original function is lost, which can cause issues with debugging and documentation.

Resources:
- functools.wraps: https://docs.python.org/3/library/functools.html#functools.wraps
'''