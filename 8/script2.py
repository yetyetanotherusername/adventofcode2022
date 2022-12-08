import numpy as np


def parse(filepath: str) -> np.ndarray:
    with open(filepath, "r") as file:
        lines = file.read().split("\n")
        data = np.zeros((len(lines) - 1, len(lines[0])))

        for row, line in enumerate(lines):
            if line.startswith("\n"):
                continue

            for col, num in enumerate(line.strip("\n")):
                data[row, col] = num

    return data


def compute_tree_score(data: np.ndarray, row: int, col: int) -> int:
    val = data[row, col]

    up_score = 0
    left_score = 0
    down_score = 0
    right_score = 0

    # look up
    for idx, other in enumerate(reversed(data[0:row, col])):
        up_score = idx + 1
        if other >= val:
            break

    # look left
    for idx, other in enumerate(reversed(data[row, 0:col])):
        left_score = idx + 1
        if other >= val:
            break

    # look down
    for idx, other in enumerate(data[row + 1 :, col]):
        down_score = idx + 1
        if other >= val:
            break

    # look right
    for idx, other in enumerate(data[row, col + 1 :]):
        right_score = idx + 1
        if other >= val:
            break

    return up_score * left_score * down_score * right_score


def compute_max_score(data: np.ndarray) -> int:
    scores = np.zeros(data.shape)

    for row in range(0, data.shape[0]):
        for col in range(0, data.shape[1]):
            scores[row, col] = compute_tree_score(data, row, col)

    return scores.max().max()


def main():
    data = parse("data.txt")
    print(compute_max_score(data))


if __name__ == "__main__":
    main()
