#!/usr/bin/env python3


def main():
    print("=== Player Inventory System ===")

    alice = {
        "sword": [1, 500, "weapon", "rare"],
        "potion": [5, 50, "consumable", "common"],
        "shield": [1, 200, "armor", "uncommon"],
    }
    bob = dict()

    print("\n=== Alice's Inventory ===")
    total_value = 0
    total_items = 0
    categories = dict()

    for name, data in alice.items():
        qty = data[0]
        price = data[1]
        category = data[2]
        rarity = data[3]

        print(
            f"{name} ({category}, {rarity}): "
            f"{qty}x @ {price} gold each = {qty * price} gold"
        )

        total_value += qty * price
        total_items += qty
        categories[category] = categories.get(category, 0) + qty

    print(f"\nInventory value: {total_value} gold")
    print(f"Item count: {total_items} items")
    print("Categories: ", end="")

    for category, count in categories.items():
        print(f"{category}({count}) ", end="")

    print("\n\n=== Transaction: Alice gives bob 2 potions ===")
    if alice["potion"][0] >= 2:
        alice["potion"][0] -= 2
        bob.update({"potion": [2, 50, "consumable", "common"]})
        print("Transaction successful!")
    else:
        print("Transaction failed!")

    print("\n=== Updated Inventories ===")
    print(f"Alice potions: {alice['potion'][0]}")
    print(f"Bob potions: {bob['potion'][0]}")

    print("\n=== Inventory Analytics ===")
    money = dict()
    items_count = dict()
    global_items = dict()

    money["alice"] = 0
    items_count["alice"] = 0
    for name, data in alice.items():
        money["alice"] += data[0] * data[1]
        items_count["alice"] += data[0]
        global_items[name] = global_items.get(name, 0) + data[0]

    money["bob"] = 0
    items_count["bob"] = 0
    for name, data in bob.items():
        money["bob"] += data[0] * data[1]
        items_count["bob"] += data[0]
        global_items[name] = global_items.get(name, 0) + data[0]

    rarest_name = None
    rarest_qty = None
    for name, qty in global_items.items():
        if rarest_qty is None or qty < rarest_qty:
            rarest_name = name
            rarest_qty = qty

    if money["alice"] > money["bob"]:
        print(f"Most valuable player: Alice ({money['alice']} gold)")
    else:
        print(f"Most valuable player: Bob ({money['bob']} gold)")

    if items_count["alice"] > items_count["bob"]:
        print(f"Most items: Alice ({items_count['alice']} items)")
    else:
        print(f"Most items: Bob ({items_count['bob']} items)")

    print(f"Rarest item: {rarest_name}")


if __name__ == "__main__":
    main()
