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


def main():
    commands = parse("data.txt")
    states = compute_state_evolution(commands)

    relevant_states = states[19::40]
    signal_strengths = [x[0] * x[1] for x in relevant_states]
    print(sum(signal_strengths))


if __name__ == "__main__":
    main()
