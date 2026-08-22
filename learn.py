from typing import Any, Callable
from functools import wraps
summary = lambda x, y: "Summary of them is " + str(x + y)

def func(test: Callable[[int, int], bool], x: int, y: int) -> bool:
    return test(x, y)


def wrappertest(test: Callable[[int, int], bool]) -> Callable[[int, int], bool]:
    @wraps(test)
    def inner(x: int, y: int) -> bool:
        print(f"Calling test with x={x}, y={y}")
        result = test(x, y)
        print(f"Result of test: {result}")
        return result
    return inner

test_func = wrappertest(lambda x, y: x > y)

test_func(5, 3)  # This will print debug information and return True

print("\n##################### NEW EXAMPLE #####################\n")

def wrapperwithargskwargs(test: Callable[..., bool]) -> Callable[..., bool]:
    @wraps(test)
    def inner(*args, **kwargs) -> bool:
        print(f"Calling test with args={args}, kwargs={kwargs}")
        result = test(*args, **kwargs)
        print(f"Result of test: {result}")
        return result
    return inner

testfunc2 = wrapperwithargskwargs(lambda x, y, z=0: x + y > z)

testfunc2(5, 3, z=4)  # This will print debug information and return True