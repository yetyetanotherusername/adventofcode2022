def priority(char: str) -> int:
    for prio, c in enumerate("abcdefghijklmnopqrstuvwxyz"):
        if char == c:
            return prio + 1

    for prio, c in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
        if char == c:
            return prio + 27

    raise Exception("No char match!")


class Rucksack:
    def __init__(self, contents: str):
        self.contents = contents


class Group:
    def __init__(self, lines: list):
        self.rucksacks = []

        for line in lines:
            self.rucksacks.append(Rucksack(line))

        if len(self.rucksacks) > 3:
            raise Exception("This group is bigger than 3!")

    def find_intersection(self):
        for char in self.rucksacks[0].contents:
            if (
                char in self.rucksacks[1].contents
                and char in self.rucksacks[2].contents
            ):
                self.intersection = char
                return

        raise Exception("No intersecting character found!")

    def prioritize(self):
        self.priority = priority(self.intersection)


class Groups:
    def __init__(self, groups: list[Group]):
        self.groups = groups

    def find_intersections(self):
        for group in self.groups:
            group.find_intersection()

    def prioritize(self):
        for group in self.groups:
            group.prioritize()

    def compute_sum(self):
        self.sum = 0
        for group in self.groups:
            self.sum += group.priority


def parse(filename: str) -> Groups:
    lines = []
    groups = []

    with open(filename, "r") as file:
        for line in file:
            lines.append(line.strip("\n"))

            if len(lines) == 3:
                groups.append(Group(lines))
                lines = []

    return Groups(groups)


def main():
    groups = parse("data.txt")
    groups.find_intersections()
    groups.prioritize()
    groups.compute_sum()

    print(groups.sum)


if __name__ == "__main__":
    main()
