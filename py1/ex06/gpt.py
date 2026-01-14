class Plant:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def grow(self, n=1):
        self.height += n
        print(f"{self.name} grew {n}cm")

    def info(self):
        return f"{self.name}: {self.height}cm"


class FloweringPlant(Plant):
    def __init__(self, name, height, color):
        super().__init__(name, height)
        self.color = color
        self.blooming = True

    def info(self):
        return f"{self.name}: {self.height}cm, {self.color} flowers (blooming)"


class PrizeFlower(FloweringPlant):
    def __init__(self, name, height, color, points):
        super().__init__(name, height, color)
        self.points = points

    def info(self):
        return (f"{self.name}: {self.height}cm, {self.color} flowers "
                f"(blooming), Prize points: {self.points}")


class Garden:
    def __init__(self, owner):
        self.owner = owner
        self.plants = []
        self.total_growth = 0

    def add_plant(self, plant):
        self.plants.append(plant)
        print(f"Added {plant.name} to {self.owner}'s garden")

    def grow_all(self):
        print(f"{self.owner} is helping all plants grow...")
        for p in self.plants:
            p.grow()
            self.total_growth += 1

    def generate_report(self, manager):
        print(f"=== {self.owner}'s Garden Report ===")
        print("Plants in garden:")
        for p in self.plants:
            print(f"- {p.info()}")
        print()
        stats = manager.GardenStats(self)
        type_counts = stats.count_types()
        print(f"Plants added: {len(self.plants)}, "
              f"Total growth: {self.total_growth}cm")
        print(f"Plant types: {type_counts['regular']} regular, "
              f"{type_counts['flowering']} flowering, "
              f"{type_counts['prize']} prize flowers")
        test_height = self.plants[0].height if self.plants else 0
        print("Height validation test:", manager.validate_height(test_height))


class GardenManager:

    total_gardens = 0

    class GardenStats:
        def __init__(self, garden):
            self.garden = garden

        def count_types(self):
            types = {"regular": 0, "flowering": 0, "prize": 0}
            for p in self.garden.plants:
                if isinstance(p, PrizeFlower):
                    types["prize"] += 1
                elif isinstance(p, FloweringPlant):
                    types["flowering"] += 1
                else:
                    types["regular"] += 1
            return types

        def garden_score(self):
            score = 0
            for p in self.garden.plants:
                score += p.height
                if isinstance(p, PrizeFlower):
                    score += p.points
            return score

    def __init__(self):
        self.gardens = []
        GardenManager.total_gardens += 1

    def add_garden(self, garden):
        self.gardens.append(garden)

    @staticmethod
    def validate_height(h):
        return isinstance(h, (int, float)) and h >= 0

    @classmethod
    def create_garden_network(cls, owners):
        return [cls() for _ in owners]


def main():
    manager = GardenManager()
    g1 = Garden("Alice")
    g2 = Garden("Bob")
    manager.add_garden(g1)
    manager.add_garden(g2)
    print("=== Garden Management System Demo ===\n")
    g1.add_plant(Plant("Oak Tree", 100))
    g1.add_plant(FloweringPlant("Rose", 25, "red"))
    g1.add_plant(PrizeFlower("Sunflower", 50, "yellow", 10))
    print()
    g1.grow_all()
    print()
    g1.generate_report(manager)
    alice_score = manager.GardenStats(g1).garden_score()
    bob_score = manager.GardenStats(g2).garden_score()
    print(f"Garden scores - Alice: {alice_score}, Bob: {bob_score}")
    print(f"Total gardens managed: {GardenManager.total_gardens}")


if __name__ == "__main__":
    main()
