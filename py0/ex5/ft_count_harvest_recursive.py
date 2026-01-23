def ft_count_harvest_recursive(x=None):
    days = x
    if days is None:
        days = int(input("Days until harvest: "))
    if days > 0:
        ft_count_harvest_recursive(x=days - 1)
        print(f"Day {days}")
        if x is None:
            print("Harvest time!")
