def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(
        artifacts,
        key=lambda artifact: artifact["power"],
        reverse=True,
    )


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda mage: mage["power"] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda spell: f"* {spell} *", spells))


def mage_stats(mages: list[dict]) -> dict:
    if not mages:
        return {"max_power": 0, "min_power": 0, "avg_power": 0.0}

    powers = list(map(lambda mage: mage["power"], mages))
    return {
        "max_power": max(powers),
        "min_power": min(powers),
        "avg_power": round(sum(powers) / len(powers), 2),
    }


def main() -> None:
    artifacts = [
        {"name": "Crystal Orb", "power": 85, "type": "focus"},
        {"name": "Fire Staff", "power": 92, "type": "weapon"},
        {"name": "Moon Amulet", "power": 67, "type": "charm"},
    ]
    mages = [
        {"name": "Astra", "power": 88, "element": "fire"},
        {"name": "Nox", "power": 54, "element": "shadow"},
        {"name": "Lyra", "power": 73, "element": "water"},
    ]
    spells = ["fireball", "heal", "shield"]

    print("Testing artifact sorter...")
    sorted_artifacts = artifact_sorter(artifacts)
    first_artifact = sorted_artifacts[0]
    second_artifact = sorted_artifacts[1]
    print(
        f"{first_artifact['name']} ({first_artifact['power']} power) "
        f"comes before {second_artifact['name']} "
        f"({second_artifact['power']} power)"
    )

    print("Testing power filter...")
    print(power_filter(mages, 70))

    print("Testing spell transformer...")
    print(" ".join(spell_transformer(spells)))

    print("Testing mage stats...")
    print(mage_stats(mages))


if __name__ == "__main__":
    main()
