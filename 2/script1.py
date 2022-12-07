import pandas as pd

pd.set_option("display.max_rows", None)


def main():
    data = pd.read_csv("data.txt", delimiter=" ", header=None)

    data.columns = ["opponent", "me"]
    data["opponent_numeric"] = None
    data["me_numeric"] = None

    data.loc[data.opponent == "A", "opponent_numeric"] = 1
    data.loc[data.opponent == "B", "opponent_numeric"] = 2
    data.loc[data.opponent == "C", "opponent_numeric"] = 3

    data.loc[data.me == "X", "me_numeric"] = 1
    data.loc[data.me == "Y", "me_numeric"] = 2
    data.loc[data.me == "Z", "me_numeric"] = 3

    data["outcome"] = 0

    data.loc[data.opponent_numeric == data.me_numeric, "outcome"] = 3

    data.loc[(data.opponent == "A") & (data.me == "Y"), "outcome"] = 6
    data.loc[(data.opponent == "B") & (data.me == "Z"), "outcome"] = 6
    data.loc[(data.opponent == "C") & (data.me == "X"), "outcome"] = 6

    data["score"] = data.me_numeric + data.outcome

    print(data)

    print(data.score.sum())


if __name__ == "__main__":
    main()
