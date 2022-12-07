def check_marker(string: str) -> bool:
    if not len(string) == 4:
        return False

    if string[0] in string[1:]:
        return False

    if string[1] in string[0] or string[1] in string[2:]:
        return False

    if string[2] in string[0:2] or string[2] in string[3]:
        return False

    if string[3] in string[0:3]:
        return False

    return True


def get_marker_index(string: str) -> int:
    for idx, block in enumerate([string[i : i + 4] for i in range(0, len(string) - 4)]):
        if check_marker(block):
            return idx + 4

    raise Exception("No marker found!")


def main():
    with open("data.txt", "r") as file:
        for line in file:
            print(get_marker_index(line))


if __name__ == "__main__":
    main()
