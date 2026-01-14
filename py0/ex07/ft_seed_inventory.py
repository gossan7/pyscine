def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    if unit == "packets":
        msg = f"{quantity} packets avaliable"
    elif unit == "grams":
        msg = f"{quantity} grams total"
    elif unit == "area":
        msg = f"covers {quantity} square meters"
    else:
        print("Unknown unit type")
        return
    print(f"{seed_type.capitalize()} seeds: {msg}")
