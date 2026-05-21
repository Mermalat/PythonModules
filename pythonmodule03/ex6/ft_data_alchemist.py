#!/usr/bin/env python3

import random


print("=== Game Data Alchemist ===")

players = [
    "Alice",
    "bob",
    "Charlie",
    "dylan",
    "Emma",
    "Gregory",
    "john",
    "kevin",
    "Liam",
]
capitalized_players = [player.capitalize() for player in players]
initially_capitalized_players = [
    player for player in players if player == player.capitalize()
]
score_by_player = {
    player: random.randint(50, 999) for player in capitalized_players
}
average_score = round(sum(score_by_player.values()) / len(score_by_player), 2)
high_scores = {
    player: score for player, score in score_by_player.items()
    if score > average_score
}

print(f"Initial list of players: {players}")
print(f"New list with all names capitalized: {capitalized_players}")
print(f"New list of capitalized names only: {initially_capitalized_players}")
print(f"Score dict: {score_by_player}")
print(f"Score average is {average_score}")
print(f"High scores: {high_scores}")
