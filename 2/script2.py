import pandas as pd


def main():
    data = pd.read_csv("data.txt", delimiter=" ", header=None)

    data.columns = ["opponent", "desired_outcome"]

    data["outcome"] = 0
    data.loc[data.desired_outcome == "Y", "outcome"] = 3
    data.loc[data.desired_outcome == "Z", "outcome"] = 6

    data["opponent_numeric"] = None
    data["me_numeric"] = None

    data.loc[data.opponent == "A", "opponent_numeric"] = 1
    data.loc[data.opponent == "B", "opponent_numeric"] = 2
    data.loc[data.opponent == "C", "opponent_numeric"] = 3

    data.loc[data.outcome == 3, "me_numeric"] = data.opponent_numeric
    data.loc[data.outcome == 6, "me_numeric"] = data.opponent_numeric + 1
    data.loc[data.outcome == 0, "me_numeric"] = data.opponent_numeric - 1

    data.loc[data.me_numeric == 0, "me_numeric"] = 3
    data.loc[data.me_numeric == 4, "me_numeric"] = 1

    data["score"] = data.me_numeric + data.outcome

    print(data)
    print(data.score.sum())


if __name__ == "__main__":
    main()
