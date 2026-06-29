import functools
import operator
from collections.abc import Callable
from typing import Any


def spell_reducer(spells: list[int], operation: str) -> int:
    if not spells:
        return 0

    if operation == "add":
        return functools.reduce(operator.add, spells)
    if operation == "multiply":
        return functools.reduce(operator.mul, spells)
    if operation == "max":
        return functools.reduce(
            lambda current, next_power: (
                current if operator.ge(current, next_power) else next_power
            ),
            spells,
        )
    if operation == "min":
        return functools.reduce(
            lambda current, next_power: (
                current if operator.le(current, next_power) else next_power
            ),
            spells,
        )
    raise ValueError(f"Unknown reducer operation: {operation}")


def partial_enchanter(
    base_enchantment: Callable[[int, str, str], str],
) -> dict[str, Callable[[str], str]]:
    return {
        "fire": functools.partial(base_enchantment, 50, "fire"),
        "ice": functools.partial(base_enchantment, 50, "ice"),
        "lightning": functools.partial(base_enchantment, 50, "lightning"),
    }


@functools.lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError("Fibonacci index cannot be negative")
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:
    @functools.singledispatch
    def cast_spell(spell_data: Any) -> str:
        return "Unknown spell type"

    @cast_spell.register
    def _(spell_data: int) -> str:
        return f"Damage spell: {spell_data} damage"

    @cast_spell.register
    def _(spell_data: str) -> str:
        return f"Enchantment: {spell_data}"

    @cast_spell.register(list)
    def _(spell_data: list[Any]) -> str:
        return f"Multi-cast: {len(spell_data)} spells"

    return cast_spell


def base_enchantment(power: int, element: str, target: str) -> str:
    return f"{element.title()} enchantment empowers {target} with {power}"


def main() -> None:
    spell_powers = [10, 20, 30, 40]

    print("Testing spell reducer...")
    print(f"Sum: {spell_reducer(spell_powers, 'add')}")
    print(f"Product: {spell_reducer(spell_powers, 'multiply')}")
    print(f"Max: {spell_reducer(spell_powers, 'max')}")

    print("Testing partial enchanter...")
    enchantments = partial_enchanter(base_enchantment)
    print(enchantments["fire"]("Sword"))
    print(enchantments["ice"]("Shield"))

    print("Testing memoized fibonacci...")
    print(f"Fib(0): {memoized_fibonacci(0)}")
    print(f"Fib(1): {memoized_fibonacci(1)}")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")
    print(f"Cache: {memoized_fibonacci.cache_info()}")

    print("Testing spell dispatcher...")
    dispatcher = spell_dispatcher()
    print(dispatcher(42))
    print(dispatcher("fireball"))
    print(dispatcher(["fireball", "heal", "shield"]))
    print(dispatcher({"mystery": True}))


if __name__ == "__main__":
    main()
