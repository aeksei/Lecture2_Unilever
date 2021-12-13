FILENAME = "Marketing_Spend.csv"


def get_column_values(filename: str, column: str) -> list:
    with open(filename) as f:
        colimns_list = f.readline().split(",")
        column_index = colimns_list.index(column)
        values = []
        for line in f:
            values.append(line.split(",")[column_index])

    return values


if __name__ == "__main__":
    print(get_column_values(FILENAME, "Offline Spend"))
