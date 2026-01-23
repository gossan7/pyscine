#!/usr/bin/env python3
import sys


def display_analysis(inventory: dict, items: int):
    """
    Display a high-level analysis of the inventory.

    This function prints the total number of items stored in the
    inventory and the number of unique item types.

    Args:
        inventory (dict): Dictionary mapping item names to quantities.
        items (int): Total number of items across all inventory entries.
    """
    print("=== Inventory System Analysis ===")
    print(f"Total items in inventory: {items}")
    print(f"Unique item types: {len(inventory)}")
    print()


def display_inventory(inventory: dict, items: int):
    """
    Display the current inventory with quantities and percentages.

    Items are sorted by quantity in descending order. For each item,
    the function prints its quantity and its percentage of the total
    inventory.

    Args:
        inventory (dict): Dictionary mapping item names to quantities.
        items (int): Total number of items across all inventory entries.
    """
    print("=== Current Inventory ===")
    inventory_list = [(item, inventory[item]) for item in inventory]
    inventory_list.sort(reverse=True, key=lambda x: x[1])
    for item, units in inventory_list:
        print(f"{item}: {units} units ({(units / items) * 100:.1f}%)")

    print()


def display_statistics(inventory: dict):
    """
    Display inventory statistics.

    This function identifies and prints the most abundant and least
    abundant items in the inventory based on their quantities.

    Args:
        inventory (dict): Dictionary mapping item names to quantities.
    """
    print("=== Inventory Statistics ===")

    most = max(inventory, key=lambda x: inventory[x])
    least = min(inventory, key=lambda x: inventory[x])

    print(f"Most abundant: {most} ({inventory[most]}",
          "units)" if inventory[most] > 1 else "unit)")

    print(f"Least abundant: {least} ({inventory[least]}",
          "units)" if inventory[least] > 1 else "unit)")

    print()


def display_categories(inventory: dict, items: int):
    """
    Categorize inventory items by abundance.

    Items are grouped into categories (Common, Moderate, Scarce)
    according to their quantities relative to the total number of
    items in the inventory.

    Args:
        inventory (dict): Dictionary mapping item names to quantities.
        items (int): Total number of items across all inventory entries.
    """
    print("=== Item Categories ===")
    moderate_threshold = items / 3
    common_threshold = items / 2

    scarce, moderate, common = dict(), dict(), dict()
    for item in inventory:
        if inventory[item] >= common_threshold:
            common[item] = inventory[item]
        elif inventory[item] >= moderate_threshold:
            moderate[item] = inventory[item]
        else:
            scarce[item] = inventory[item]
    if common:
        print(f"Common: {common}")
    if moderate:
        print(f"Moderate: {moderate}")
    if scarce:
        print(f"Scarce: {scarce}")
    print()


def display_suggestions(inventory: dict):
    """
    Display inventory management suggestions.

    This function identifies items that may need restocking by
    selecting the least abundant items in the inventory.

    Args:
        inventory (dict): Dictionary mapping item names to quantities.
    """
    n_restock = round(len(inventory) / 3)
    inventory_list = [item for item in inventory]
    inventory_list.sort(key=lambda x: inventory[x])
    print(f"Restock needed: {inventory_list[:n_restock]}")
    print()


def display_properties(inventory: dict):
    """
    Demonstrate dictionary properties and operations.

    This function displays the dictionary keys and values and
    demonstrates a sample lookup to show how dictionaries provide
    fast access to stored data.

    Args:
        inventory (dict): Dictionary mapping item names to quantities.
    """
    print("=== Dictionary Properties Demo ===")
    print(f"Dictionary keys: {list(inventory.keys())}")
    print(f"Dictionary values: {list(inventory.values())}")
    print(f"Sample lookup - 'sword' in inventory: {'sword' in inventory}")


def main():
    """
    Parse command-line arguments and manage the inventory system.

    This function builds the inventory from command-line input,
    computes inventory statistics, categorizes items by abundance,
    provides restocking suggestions, and demonstrates dictionary
    properties.
    """
    inventory = dict()
    items = 0
    for arg in sys.argv[1:]:
        try:
            item, units = arg.split(":")
            units = int(units)
            inventory[item] = units
            items += units
        except Exception as e:
            print(f"Error occured during parsing: {e}")
            return

    display_analysis(inventory, items)
    display_inventory(inventory, items)
    display_statistics(inventory)
    display_categories(inventory, items)
    display_suggestions(inventory)
    display_properties(inventory)


if __name__ == "__main__":
    main()
