def parse(filepath: str) -> dict:
    with open(filepath, "r") as file:
        blocks = file.read().split("\n\n")

        monkeys = {}

        for block in blocks:
            lines = block.split("\n")

            index = int(lines[0].split(" ")[1].strip(":"))
            items = [int(x) for x in lines[1].split(":")[1].split(",")]

            operation = tuple(lines[2].split("=")[1].split(" "))

            test = int(lines[3].split("by ")[1])
            if_true = int(lines[4].split("monkey ")[1])
            if_false = int(lines[5].split("monkey ")[1])

            monkeys[index] = {
                "items": items,
                "operation": operation,
                "test": test,
                "true": if_true,
                "false": if_false,
                "counter": 0,
            }

    return monkeys


def perform_operation(old: int, operation: tuple) -> int:
    operator = operation[2]
    operand2 = operation[3]

    if operand2 == "old":
        operand2 = old
    else:
        operand2 = int(operand2)

    if operator == "*":
        return old * operand2
    else:
        return old + operand2


def perform_round(monkeys: dict):
    for monkey in monkeys.values():
        for item in monkey["items"]:
            monkey["counter"] += 1
            new_item = perform_operation(item, monkey["operation"]) // 3
            if new_item % monkey["test"] == 0:
                monkeys[monkey["true"]]["items"].append(new_item)
            else:
                monkeys[monkey["false"]]["items"].append(new_item)

        monkey["items"] = []


def main():
    rounds = 20
    monkeys = parse("data.txt")

    for _ in range(rounds):
        perform_round(monkeys)

    monkeys = {
        k: v
        for k, v in sorted(
            monkeys.items(), key=lambda item: item[1]["counter"], reverse=True
        )
    }

    monkey_business = (
        list(monkeys.items())[0][1]["counter"] * list(monkeys.items())[1][1]["counter"]
    )
    print(monkey_business)


if __name__ == "__main__":
    main()
