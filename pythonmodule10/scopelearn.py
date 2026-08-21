from collections.abc import Callable
from time import sleep

def spell_accumulator(initial_power: int) -> Callable[[int], int]:
    total_power = initial_power

    def add_power(amount: int) -> int:
        nonlocal total_power
        total_power += amount
        return total_power

    return add_power

test = spell_accumulator(100)
print(test(25))
sleep(1)
