def parse(filepath: str) -> list[str]:
    with open(filepath, "r") as file:
        return file.read().split("\n")[:-1]


def compute_state_evolution(commands: list[str]) -> list[tuple[int, int]]:
    state = []
    cycle_count = 1
    register = 1

    for line in commands:
        if line.startswith("noop"):
            state.append((cycle_count, register))
            cycle_count += 1

        else:
            value = line.split(" ")[1]
            state.append((cycle_count, register))
            cycle_count += 1
            state.append((cycle_count, register))
            cycle_count += 1
            register += int(value)

    return state


def intersection(state: tuple) -> bool:
    index, register = state
    index %= 40
    index -= 1

    if index - 1 <= register <= index + 1:
        return True

    return False


def check_intersections(states: list[tuple[int, int]]) -> str:
    return "".join(["#" if intersection(state) else "." for state in states])


def print_output(pixels: str) -> None:
    for line in [pixels[i : i + 40] for i in range(0, len(pixels), 40)]:
        print(line)


def main():
    commands = parse("data.txt")
    states = compute_state_evolution(commands)

    pixels = check_intersections(states)
    print_output(pixels)


if __name__ == "__main__":
    main()
