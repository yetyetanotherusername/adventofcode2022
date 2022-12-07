def priority(char: str) -> int:
    for prio, c in enumerate("abcdefghijklmnopqrstuvwxyz"):
        if char == c:
            return prio + 1

    for prio, c in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
        if char == c:
            return prio + 27

    raise Exception("No char match!")


class Compartment:
    def __init__(self, contents):
        self.contents = contents


class Rucksack:
    def __init__(self, contents):
        content_len = len(contents)
        compartment_len = content_len // 2

        self.compartments = [
            Compartment(contents[:compartment_len]),
            Compartment(contents[compartment_len:]),
        ]

    def find_intersection(self):
        for char in self.compartments[0].contents:
            if char in self.compartments[1].contents:
                self.intersection = char
                return

        raise Exception("No matching chars found in compartments!")

    def prioritize(self):
        self.priority = priority(self.intersection)


class Rucksacks:
    def __init__(self, rucksacks):
        self.rucksacks = rucksacks

    def find_intersections(self):
        for rucksack in self.rucksacks:
            rucksack.find_intersection()

    def prioritize(self):
        for rucksack in self.rucksacks:
            rucksack.prioritize()

    def compute_sum(self):
        self.sum = 0
        for rucksack in self.rucksacks:
            self.sum += rucksack.priority


def parse(filename: str) -> Rucksacks:
    with open(filename, "r") as file:
        return Rucksacks([Rucksack(line.strip("\n")) for line in file])


def main():
    rucksacks = parse("data.txt")
    rucksacks.find_intersections()
    rucksacks.prioritize()
    rucksacks.compute_sum()

    print(rucksacks.sum)


if __name__ == "__main__":
    main()
