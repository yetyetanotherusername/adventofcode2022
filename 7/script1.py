class File:
    def __init__(self, size: int, name: str) -> None:
        self.size = size
        self.name = name


class Directory:
    def __init__(self, name: str, parent=None) -> None:
        self.name = name
        self.parent = parent
        self.contents: list[Directory | File] = []
        self.contents_size = 0

    def calc_size(self):
        for item in self.contents:
            if isinstance(item, File):
                self.contents_size += item.size
            else:
                item.calc_size()
                self.contents_size += item.contents_size

    def calc_sum(self):
        local_sum = 0

        if self.contents_size < 100000:
            local_sum += self.contents_size

        for item in self.contents:
            if not isinstance(item, File):
                local_sum += item.calc_sum()

        return local_sum


filesystem = Directory("/")
current_directory = filesystem


def cd(argument: str):
    global current_directory

    if argument == "/":
        return

    if argument == "..":
        parent = current_directory.parent
        current_directory = parent
        return

    current_directory.contents.append(
        Directory(name=argument, parent=current_directory)
    )
    current_directory = current_directory.contents[-1]


def execute_command(command: str):
    if command.startswith("cd"):
        cd(command[3:])
        return

    if command.startswith("ls"):
        return

    raise Exception("Unknown command!")


def parse(input_path: str) -> None:
    with open(input_path, "r") as file:
        for line in file:
            line = line.strip("\n")

            # is command
            if line.startswith("$"):
                execute_command(line[2:])
                continue

            # is file
            if line[0] in "0123456789":
                split = line.split(" ")
                current_directory.contents.append(
                    File(size=int(split[0]), name=split[1])
                )
                continue

            # is directory contents
            if line.startswith("dir"):
                continue


def main():
    parse("data.txt")

    filesystem.calc_size()

    print(filesystem.calc_sum())


if __name__ == "__main__":
    main()
