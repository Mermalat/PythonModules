class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name
        self._height = 0.0
        self._age = 0
        self.set_height(height)
        self.set_age(age)

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

    def age(self, days: int) -> None:
        self._age += days

    def show(self) -> None:
        print(
            self._name + ": " + str(round(self._height, 1))
            + "cm, " + str(self._age) + " days old"
        )


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
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        trunk_diameter: float,
    ) -> None:
        super().__init__(name, height, age)
        self._trunk_diameter = float(trunk_diameter)

    def produce_shade(self) -> None:
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


def main() -> None:
    print("=== Garden Plant Types ===")

    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    print("[asking the rose to bloom]")
    rose.bloom()
    rose.show()

    print("=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    print("[asking the oak to produce shade]")
    oak.produce_shade()

    print("=== Vegetable")
    tomato = Vegetable("Tomato", 5.0, 10, "April")
    tomato.show()
    print("[make tomato grow and age for 20 days]")
    tomato.grow(42.0)
    tomato.age(20)
    tomato.show()


if __name__ == "__main__":
    main()
