from collections.abc import Callable


def ensure_spell(spell: Callable[[str, int], str]) -> None:
    if not callable(spell):
        raise TypeError("Expected a callable spell")


def spell_combiner(
    spell1: Callable[[str, int], str],
    spell2: Callable[[str, int], str],
) -> Callable[[str, int], tuple[str, str]]:
    ensure_spell(spell1)
    ensure_spell(spell2)

    def combined_spell(target: str, power: int) -> tuple[str, str]:
        return spell1(target, power), spell2(target, power)

    return combined_spell


def power_amplifier(
    base_spell: Callable[[str, int], str],
    multiplier: int,
) -> Callable[[str, int], str]:
    ensure_spell(base_spell)

    def amplified_spell(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)

    return amplified_spell


def conditional_caster(
    condition: Callable[[str, int], bool],
    spell: Callable[[str, int], str],
) -> Callable[[str, int], str]:
    ensure_spell(spell)

    def conditional_spell(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        return "Spell fizzled"

    return conditional_spell


def spell_sequence(
    spells: list[Callable[[str, int], str]],
) -> Callable[[str, int], list[str]]:
    for spell in spells:
        ensure_spell(spell)

    def sequenced_spell(target: str, power: int) -> list[str]:
        return [spell(target, power) for spell in spells]

    return sequenced_spell


def fireball(target: str, power: int) -> str:
    return f"Fireball hits {target} for {power} damage"


def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"


def shield(target: str, power: int) -> str:
    return f"Shield protects {target} with {power} power"


def main() -> None:
    print("Testing spell combiner...")
    combined = spell_combiner(fireball, heal)
    combined_result = combined("Dragon", 20)
    print(f"Combined spell result: {combined_result[0]}, {combined_result[1]}")

    print("Testing power amplifier...")
    mega_fireball = power_amplifier(fireball, 3)
    print(f"Original: 10, Amplified: {mega_fireball('Dragon', 10)}")

    print("Testing conditional caster...")
    safe_fireball = conditional_caster(
        lambda target, power: power >= 15,
        fireball,
    )
    print(safe_fireball("Dragon", 20))
    print(safe_fireball("Dragon", 8))

    print("Testing spell sequence...")
    sequence = spell_sequence([fireball, heal, shield])
    print(sequence("Knight", 12))


if __name__ == "__main__":
    main()
