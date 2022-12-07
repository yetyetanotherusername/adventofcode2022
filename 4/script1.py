class Elf:
    def __init__(self, assignment: str) -> None:
        self.assignment_raw = assignment

    def unwrangle_assignment(self):
        start, stop = self.assignment_raw.split("-")
        self.start = int(start)
        self.stop = int(stop)

        self.assignment = [x for x in range(self.start, self.stop + 1)]

    def get_len(self) -> int:
        return len(self.assignment)

    def check(self, other) -> bool:
        if self.get_len() > other.get_len():
            return False

        for num in self.assignment:
            if not num in other.assignment:
                return False

        return True


class Pair:
    def __init__(self, elves: list[Elf]) -> None:
        self.elves = elves
        self.duplicate = False

    def unwrangle(self):
        for elf in self.elves:
            elf.unwrangle_assignment()

    def check_assignments(self):
        check1 = self.elves[0].check(self.elves[1])
        check2 = self.elves[1].check(self.elves[0])

        self.duplicate = check1 or check2


class Pairs:
    def __init__(self, pairs: list[Pair]) -> None:
        self.pairs = pairs
        self.sum = 0

    def unwrangle(self):
        for pair in self.pairs:
            pair.unwrangle()

    def check(self):
        for pair in self.pairs:
            pair.check_assignments()

    def compute_sum(self):
        for pair in self.pairs:
            self.sum += pair.duplicate


def parse(filepath: str) -> Pairs:
    pairs = []

    with open(filepath, "r") as file:
        for line in file:
            assignments = line.split(",")
            pair = Pair([Elf(assignments[0]), Elf(assignments[1])])
            pairs.append(pair)

    return Pairs(pairs)


def main():
    pairs = parse("data.txt")
    pairs.unwrangle()
    pairs.check()
    pairs.compute_sum()

    print(pairs.sum)


if __name__ == "__main__":
    main()
