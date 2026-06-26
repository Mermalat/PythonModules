from ex0 import AquaFactory, CreatureFactory, FlameFactory
from ex0.creatures import Creature
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import (
    AggressiveStrategy,
    BattleStrategy,
    DefensiveStrategy,
    InvalidStrategyError,
    NormalStrategy,
)

Opponent = tuple[CreatureFactory, BattleStrategy]


def run_strategy(creature: Creature, strategy: BattleStrategy) -> None:
    for action in strategy.act(creature):
        print(action)


def battle_tournament(opponents: list[Opponent]) -> None:
    creatures = [
        (factory.create_base(), strategy)
        for factory, strategy in opponents
    ]

    print("*** Tournament ***")
    print(f"{len(creatures)} opponents involved")

    try:
        for index, first in enumerate(creatures):
            first_creature, first_strategy = first
            for second_creature, second_strategy in creatures[index + 1:]:
                print("* Battle *")
                print(first_creature.describe())
                print("vs.")
                print(second_creature.describe())
                print("now fight!")
                run_strategy(first_creature, first_strategy)
                run_strategy(second_creature, second_strategy)
    except InvalidStrategyError as error:
        print(f"Battle error, aborting tournament: {error}")


def print_tournament_header(number: int, label: str, opponents: str) -> None:
    print(f"Tournament {number} ({label})")
    print(opponents)


def main() -> None:
    normal = NormalStrategy()
    aggressive = AggressiveStrategy()
    defensive = DefensiveStrategy()

    print_tournament_header(
        0,
        "basic",
        "[ (Flameling+Normal), (Healing+Defensive) ]",
    )
    battle_tournament([
        (FlameFactory(), normal),
        (HealingCreatureFactory(), defensive),
    ])

    print_tournament_header(
        1,
        "error",
        "[ (Flameling+Aggressive), (Healing+Defensive) ]",
    )
    battle_tournament([
        (FlameFactory(), aggressive),
        (HealingCreatureFactory(), defensive),
    ])

    print_tournament_header(
        2,
        "multiple",
        "[ (Aquabub+Normal), (Healing+Defensive), "
        "(Transform+Aggressive) ]",
    )
    battle_tournament([
        (AquaFactory(), normal),
        (HealingCreatureFactory(), defensive),
        (TransformCreatureFactory(), aggressive),
    ])


if __name__ == "__main__":
    main()
