from ex0.creatures import Creature
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex1.capabilities import HealCapability, TransformCapability


def test_healing_creature(creature: Creature) -> None:
    if not isinstance(creature, HealCapability):
        print(f"{creature.name} cannot heal.")
        return
    print(creature.describe())
    print(creature.attack())
    print(creature.heal())


def test_transforming_creature(creature: Creature) -> None:
    if not isinstance(creature, TransformCapability):
        print(f"{creature.name} cannot transform.")
        return
    print(creature.describe())
    print(creature.attack())
    print(creature.transform())
    print(creature.attack())
    print(creature.revert())


def main() -> None:
    healing_factory = HealingCreatureFactory()
    transform_factory = TransformCreatureFactory()

    print("Testing Creature with healing capability")
    print("base:")
    test_healing_creature(healing_factory.create_base())
    print("evolved:")
    test_healing_creature(healing_factory.create_evolved())

    print("Testing Creature with transform capability")
    print("base:")
    test_transforming_creature(transform_factory.create_base())
    print("evolved:")
    test_transforming_creature(transform_factory.create_evolved())


if __name__ == "__main__":
    main()
