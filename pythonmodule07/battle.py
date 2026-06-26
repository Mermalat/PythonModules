from ex0 import AquaFactory, CreatureFactory, FlameFactory
from ex0.creatures import Creature


def test_factory(factory: CreatureFactory) -> None:
    print("Testing factory")
    for creature in (factory.create_base(), factory.create_evolved()):
        print(creature.describe())
        print(creature.attack())


def test_battle(
    first_factory: CreatureFactory,
    second_factory: CreatureFactory,
) -> None:
    first_creature: Creature = first_factory.create_base()
    second_creature: Creature = second_factory.create_base()

    print("Testing battle")
    print(first_creature.describe())
    print("vs.")
    print(second_creature.describe())
    print("fight!")
    print(first_creature.attack())
    print(second_creature.attack())


def main() -> None:
    flame_factory = FlameFactory()
    aqua_factory = AquaFactory()

    test_factory(flame_factory)
    test_factory(aqua_factory)
    test_battle(flame_factory, aqua_factory)


if __name__ == "__main__":
    main()
