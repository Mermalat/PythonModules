#!/usr/bin/env python3

import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        raw_pos = input("Enter new coordinates as floats in format 'x,y,z': ")
        parts = raw_pos.split(",")

        if len(parts) != 3:
            print("Invalid syntax")
            continue

        try:
            x_pos = float(parts[0])
            y_pos = float(parts[1])
            z_pos = float(parts[2])
            return (x_pos, y_pos, z_pos)
        except ValueError as error:
            bad_index = 0
            while bad_index < len(parts):
                try:
                    float(parts[bad_index])
                except ValueError:
                    print(
                        "Error on parameter "
                        f"'{parts[bad_index].strip()}': {error}"
                    )
                    break
                bad_index += 1


def get_distance(
    first_pos: tuple[float, float, float],
    second_pos: tuple[float, float, float],
) -> float:
    return math.sqrt(
        (second_pos[0] - first_pos[0]) ** 2
        + (second_pos[1] - first_pos[1]) ** 2
        + (second_pos[2] - first_pos[2]) ** 2
    )


print("=== Game Coordinate System ===")
print("Get a first set of coordinates")
first_position = get_player_pos()
print(f"Got a first tuple: {first_position}")
print(
    "It includes: "
    f"X={first_position[0]}, Y={first_position[1]}, Z={first_position[2]}"
)
center_distance = get_distance((0, 0, 0), first_position)
print(f"Distance to center: {round(center_distance, 4)}")

print("Get a second set of coordinates")
second_position = get_player_pos()
distance = get_distance(first_position, second_position)
print(f"Distance between the 2 sets of coordinates: {round(distance, 4)}")
