#!/usr/bin/env python3

import sys


print("=== Inventory System Analysis ===")

inventory: dict[str, int] = {}

index = 1
while index < len(sys.argv):
    parameter = sys.argv[index]
    parts = parameter.split(":")

    if len(parts) != 2 or parts[0] == "":
        print(f"Error - invalid parameter '{parameter}'")
    elif parts[0] in inventory.keys():
        print(f"Redundant item '{parts[0]}' - discarding")
    else:
        try:
            inventory[parts[0]] = int(parts[1])
        except ValueError as error:
            print(f"Quantity error for '{parts[0]}': {error}")

    index += 1

print(f"Got inventory: {inventory}")

item_list = list(inventory.keys())
quantity_list = list(inventory.values())
total_quantity = sum(quantity_list)

print(f"Item list: {item_list}")
print(f"Total quantity of the {len(item_list)} items: {total_quantity}")

for item in inventory.keys():
    if total_quantity == 0:
        item_percent = 0.0
    else:
        item_percent = round(inventory[item] * 100 / total_quantity, 1)
    print(f"Item {item} represents {item_percent}%")

if len(item_list) > 0:
    most_abundant = item_list[0]
    least_abundant = item_list[0]

    for item in inventory.keys():
        if inventory[item] > inventory[most_abundant]:
            most_abundant = item
        if inventory[item] < inventory[least_abundant]:
            least_abundant = item

    print(
        "Item most abundant: "
        f"{most_abundant} with quantity {inventory[most_abundant]}"
    )
    print(
        "Item least abundant: "
        f"{least_abundant} with quantity {inventory[least_abundant]}"
    )

inventory.update({"magic_item": 1})
print(f"Updated inventory: {inventory}")
