import math


class Coordinate:
    def __init__(self):
        self.x = 0
        self.y = 0


class State:
    def __init__(self):
        self.state = [Coordinate() for _ in range(10)]


def parse(filename: str) -> list[str]:
    with open(filename, "r") as file:
        return file.read().split("\n")


def euclidean_distance(this: Coordinate, other: Coordinate) -> float:
    return math.sqrt((this.x - other.x) ** 2 + (this.y - other.y) ** 2)


def norm(num: int):
    if num == 0:
        return 0
    elif num > 0:
        return 1
    else:
        return -1


def follow(state: State):
    for idx in range(0, 9):
        d2 = euclidean_distance(state.state[idx + 1], state.state[idx])
        if d2 > math.sqrt(2):
            pull_vector = (
                state.state[idx].x - state.state[idx + 1].x,
                state.state[idx].y - state.state[idx + 1].y,
            )

            state.state[idx + 1].x += norm(pull_vector[0])
            state.state[idx + 1].y += norm(pull_vector[1])


def up(state: State):
    state.state[0].x += 1


def left(state: State):
    state.state[0].y -= 1


def down(state: State):
    state.state[0].x -= 1


def right(state: State):
    state.state[0].y += 1


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
        follow(state)
        tail_positions.append((state.state[9].x, state.state[9].y))


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
