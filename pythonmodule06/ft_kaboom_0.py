import alchemy.grimoire


def main() -> None:
    print("=== Kaboom 0 ===")
    print("Using grimoire module directly")
    recorded_spell = alchemy.grimoire.light_spell_record(
        "Fantasy",
        "Earth, wind and fire",
    )
    print(
        "Testing record light spell: "
        f"{recorded_spell}"
    )


if __name__ == "__main__":
    main()
