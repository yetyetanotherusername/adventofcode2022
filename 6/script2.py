from collections import Counter


def check_marker(string: str) -> bool:
    freq = Counter(string)

    if len(freq) == len(string):
        return True
    else:
        return False


def get_marker_index(string: str, sequence_len=14) -> int:
    for idx, block in enumerate(
        [string[i : i + sequence_len] for i in range(0, len(string) - sequence_len)]
    ):
        if check_marker(block):
            return idx + sequence_len

    raise Exception("No marker found!")


def main():
    with open("data.txt", "r") as file:
        for line in file:
            print(get_marker_index(line))


if __name__ == "__main__":
    main()
