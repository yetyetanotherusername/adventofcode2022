from queue import LifoQueue


class Stack:
    def __init__(self) -> None:
        self.stack = LifoQueue()

    def store(self, crate: str):
        self.stack.put(crate)

    def remove(self) -> str:
        return self.stack.get()


def parse_stacks(filepath: str, num_stacks: int) -> list[Stack]:
    stacks = []
    for idx in range(num_stacks):
        stacks.append(Stack())

    with open(filepath, "r") as file:
        for line in reversed(list(file)):
            crates = [line[i : i + 4] for i in range(0, len(line), 4)]

            for idx, crate in enumerate(crates):
                if crate.startswith("["):
                    stacks[idx].store(crate.strip(" "))

    return stacks


def parse_commands(filepath: str, start_line: int) -> list[tuple[int, int, int]]:
    commands = []

    with open(filepath, "r") as file:
        for idx, line in enumerate(file):
            if idx + 1 < start_line:
                continue

            split = line.split(" ")

            commands.append((int(split[1]), int(split[3]), int(split[5])))

    return commands


def apply_commands(
    stacks: list[Stack], commands: list[tuple[int, int, int]]
) -> list[Stack]:
    for command in commands:
        repeats = command[0]
        from_stack = command[1] - 1
        to_stack = command[2] - 1

        temp_stack = []

        for _ in range(0, repeats):
            temp_stack.append(stacks[from_stack].remove())

        for crate in reversed(temp_stack):
            stacks[to_stack].store(crate)

    return stacks


def main():
    filepath = "data.txt"
    num_stacks = 9
    command_start_line = 11

    stacks = parse_stacks(filepath, num_stacks)
    commands = parse_commands(filepath, command_start_line)
    stacks = apply_commands(stacks, commands)

    for stack in stacks:
        print(stack.remove())


if __name__ == "__main__":
    main()
