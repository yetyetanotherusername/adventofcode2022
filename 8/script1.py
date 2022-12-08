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


def compute_circumference(data: np.ndarray) -> int:
    return data.shape[0] * 2 - 2 + data.shape[1] * 2 - 2


def is_tree_visible(data: np.ndarray, row: int, col: int) -> bool:
    val = data[row, col]

    # check left
    left = max(data[row, :col])
    if left < val:
        return True

    # check right
    right = max(data[row, col + 1 :])
    if right < val:
        return True

    # check down
    down = max(data[row + 1 :, col])
    if down < val:
        return True

    # check up
    up = max(data[:row, col])
    if up < val:
        return True

    return False


def compute_visible(data: np.ndarray) -> int:
    vis_mask = np.zeros(data.shape)

    for row in range(1, data.shape[0] - 1):
        for col in range(1, data.shape[1] - 1):
            if is_tree_visible(data, row, col):
                vis_mask[row, col] = 1

    return vis_mask.sum().sum()


def main():
    visible = 0
    data = parse("data.txt")

    visible += compute_circumference(data)
    visible += compute_visible(data)

    print(visible)


if __name__ == "__main__":
    main()
