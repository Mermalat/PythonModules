#!/usr/bin/env python3

import random


ACHIEVEMENTS = [
    "First Steps",
    "Master Explorer",
    "Treasure Hunter",
    "Boss Slayer",
    "Crafting Genius",
    "Speed Runner",
    "Survivor",
    "Collector Supreme",
    "Untouchable",
    "World Savior",
    "Hidden Path Finder",
    "Strategist",
    "Unstoppable",
    "Sharp Mind",
]
OPTIONAL_ACHIEVEMENTS = [
    "First Steps",
    "Master Explorer",
    "Treasure Hunter",
    "Boss Slayer",
    "Crafting Genius",
    "Speed Runner",
    "Survivor",
    "Collector Supreme",
    "World Savior",
    "Hidden Path Finder",
    "Strategist",
    "Unstoppable",
    "Sharp Mind",
]


def gen_player_achievements() -> set[str]:
    achievement_count = random.randint(5, 9)
    achievements = set(
        random.sample(OPTIONAL_ACHIEVEMENTS, achievement_count - 1)
    )
    achievements.add("Untouchable")
    return achievements


print("=== Achievement Tracker System ===")

players = ["Alice", "Bob", "Charlie", "Dylan"]
player_achievements: dict[str, set[str]] = {}

for player in players:
    player_achievements[player] = gen_player_achievements()
    print(f"Player {player}: {player_achievements[player]}")

all_achievements = set()
common_achievements = set(ACHIEVEMENTS)

for player in players:
    all_achievements = all_achievements.union(player_achievements[player])
    common_achievements = common_achievements.intersection(
        player_achievements[player]
    )

print(f"All distinct achievements: {all_achievements}")
print(f"Common achievements: {common_achievements}")

for player in players:
    other_achievements = set()
    for other_player in players:
        if other_player != player:
            other_achievements = other_achievements.union(
                player_achievements[other_player]
            )
    unique_achievements = player_achievements[player].difference(
        other_achievements
    )
    print(f"Only {player} has: {unique_achievements}")

for player in players:
    missing_achievements = set(ACHIEVEMENTS).difference(
        player_achievements[player]
    )
    print(f"{player} is missing: {missing_achievements}")
