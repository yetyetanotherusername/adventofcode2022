class Coordinate:
    def __init__(self):
        self.x = 0
        self.y = 0


class State:
    def __init__(self):
        self.head = Coordinate()
        self.tail = Coordinate()


def parse(filename: str) -> list[str]:
    with open(filename, "r") as file:
        return file.read().split("\n")


def up(state: State):
    state.head.x += 1

    if state.tail.x < state.head.x - 1:
        state.tail.x += 1
        state.tail.y = state.head.y


def left(state: State):
    state.head.y -= 1

    if state.tail.y > state.head.y + 1:
        state.tail.y -= 1
        state.tail.x = state.head.x


def down(state: State):
    state.head.x -= 1

    if state.tail.x > state.head.x + 1:
        state.tail.x -= 1
        state.tail.y = state.head.y


def right(state: State):
    state.head.y += 1

    if state.tail.y < state.head.y - 1:
        state.tail.y += 1
        state.tail.x = state.head.x


def apply_command(state: State, command: str, tail_positions: list[tuple[int, int]]):
    direction, distance = command.split(" ")

    match direction:
        case "U":
            function = up
        case "L":
            function = left
        case "D":
            function = down
        case "R":
            function = right
        case _:
            raise Exception("Unknown direction!")

    for _ in range(int(distance)):
        function(state)
        tail_positions.append((state.tail.x, state.tail.y))


def main():
    state = State()
    tail_positions = [(0, 0)]
    lines = parse("data.txt")

    for line in lines:
        if line == "":
            break
        apply_command(state, line, tail_positions)

    print(len(list(set(tail_positions))))


if __name__ == "__main__":
    main()
