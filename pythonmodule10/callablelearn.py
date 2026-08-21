from collections.abc import callable, Callable

# Can you give me an example of how to use the callable functions?
# But not like this fantastic thing, I want more simple examples, like a function that takes another function as an argument and calls it.
# Sure! Here are some simple examples of how to use callable functions in Python:

def greet(name: str) -> str:
    return f"Hello, {name}!"

# A function that takes another function as an argument and calls it
def call_function(func: Callable[[str], str], arg: str) -> str:
    return func(arg)

# Why did we use Callable[[str], str] in the type hint for func?
# We used `Callable[[str], str]` in the type hint for `func` to indicate that `func` is expected to be a callable (function) that takes a single argument of type `str` and returns a value of type `str`.
# This helps with type checking and makes the code more readable by specifying the expected input and output types of the function being passed as an argument.

# Example usage
result = call_function(greet, "Alice")
print(result)  # Output: Hello, Alice!

def spell_combiner(
    spell1: Callable[[str, int], str],
    spell2: Callable[[str, int], str]
) -> Callable[[str, int], tuple[str, str]]:
    ensure_spell(spell1)
    ensure_spell(spell2)

    def combined_spell(target: str, power: int) -> tuple[str, str]:
        return spell1(target, power), spell2(target, power)

    return combined_spell

# in callable does big c or small c matters?
# In Python, the `callable` function is case-sensitive, and it must be written in lowercase. The `Callable` type hint from the `collections.abc` module is also case-sensitive and should be written with a capital "C".
# so is it wrong to write callable with a capital C?
# Yes, it is incorrect to write `callable` with a capital "C". The correct usage is `callable` (lowercase) when checking if an object is callable, and `Callable` (uppercase) when using it as a type hint.
