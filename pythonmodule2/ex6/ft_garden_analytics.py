class Plant:
    class Statistics:
        def __init__(self) -> None:
            self._grow_calls = 0
            self._age_calls = 0
            self._show_calls = 0

        def add_grow(self) -> None:
            self._grow_calls += 1

        def add_age(self) -> None:
            self._age_calls += 1

        def add_show(self) -> None:
            self._show_calls += 1

        def show(self) -> None:
            print(
                "Stats: " + str(self._grow_calls) + " grow, "
                + str(self._age_calls) + " age, "
                + str(self._show_calls) + " show"
            )

    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name
        self._height = 0.0
        self._age = 0
        self._stats = Plant.Statistics()
        self.set_height(height)
        self.set_age(age)

    @staticmethod
    def is_older_than_year(age: int) -> bool:
        return age > 365

    @classmethod
    def anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0)

    def set_height(self, height: float) -> bool:
        if height < 0:
            print(self._name + ": Error, height can't be negative")
            return False
        self._height = float(height)
        return True

    def set_age(self, age: int) -> bool:
        if age < 0:
            print(self._name + ": Error, age can't be negative")
            return False
        self._age = age
        return True

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def grow(self, amount: float) -> None:
        self._height += amount
        self._stats.add_grow()

    def age(self, days: int) -> None:
        self._age += days
        self._stats.add_age()

    def show(self) -> None:
        self._stats.add_show()
        print(
            self._name + ": " + str(round(self._height, 1))
            + "cm, " + str(self._age) + " days old"
        )

    def show_statistics(self) -> None:
        self._stats.show()


class Flower(Plant):
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        color: str,
    ) -> None:
        super().__init__(name, height, age)
        self._color = color
        self._has_bloomed = False

    def bloom(self) -> None:
        self._has_bloomed = True

    def show(self) -> None:
        super().show()
        print("Color: " + self._color)
        if self._has_bloomed:
            print(self._name + " is blooming beautifully!")
        else:
            print(self._name + " has not bloomed yet")


class Tree(Plant):
    class TreeStatistics(Plant.Statistics):
        def __init__(self) -> None:
            super().__init__()
            self._shade_calls = 0

        def add_shade(self) -> None:
            self._shade_calls += 1

        def show(self) -> None:
            super().show()
            print(str(self._shade_calls) + " shade")

    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        trunk_diameter: float,
    ) -> None:
        super().__init__(name, height, age)
        self._stats = Tree.TreeStatistics()
        self._trunk_diameter = float(trunk_diameter)

    def produce_shade(self) -> None:
        self._stats.add_shade()
        print(
            "Tree " + self._name + " now produces a shade of "
            + str(round(self._height, 1)) + "cm long and "
            + str(round(self._trunk_diameter, 1)) + "cm wide."
        )

    def show(self) -> None:
        super().show()
        print("Trunk diameter: " + str(round(self._trunk_diameter, 1)) + "cm")


class Vegetable(Plant):
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        harvest_season: str,
    ) -> None:
        super().__init__(name, height, age)
        self._harvest_season = harvest_season
        self._nutritional_value = 0

    def grow(self, amount: float) -> None:
        super().grow(amount)
        self._nutritional_value += 10

    def age(self, days: int) -> None:
        super().age(days)
        self._nutritional_value += 10

    def show(self) -> None:
        super().show()
        print("Harvest season: " + self._harvest_season)
        print("Nutritional value: " + str(self._nutritional_value))


class Seed(Flower):
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        color: str,
    ) -> None:
        super().__init__(name, height, age, color)
        self._seeds = 0

    def bloom(self) -> None:
        super().bloom()
        self._seeds = 42

    def show(self) -> None:
        super().show()
        print("Seeds: " + str(self._seeds))


def display_statistics(plant: Plant) -> None:
    print("[statistics for " + plant._name + "]")
    plant.show_statistics()


def main() -> None:
    print("=== Garden statistics ===")

    print("=== Check year-old")
    print(
        "Is 30 days more than a year? -> "
        + str(Plant.is_older_than_year(30))
    )
    print(
        "Is 400 days more than a year? -> "
        + str(Plant.is_older_than_year(400))
    )

    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    display_statistics(rose)
    print("[asking the rose to grow and bloom]")
    rose.grow(8.0)
    rose.bloom()
    rose.show()
    display_statistics(rose)

    print("=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    display_statistics(oak)
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    display_statistics(oak)

    print("=== Seed")
    sunflower = Seed("Sunflower", 80.0, 45, "yellow")
    sunflower.show()
    print("[make sunflower grow, age and bloom]")
    sunflower.grow(30.0)
    sunflower.age(20)
    sunflower.bloom()
    sunflower.show()
    display_statistics(sunflower)

    print("=== Anonymous")
    unknown = Plant.anonymous()
    unknown.show()
    display_statistics(unknown)


if __name__ == "__main__":
    main()
