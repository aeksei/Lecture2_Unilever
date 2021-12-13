from typing import Union

from task_4_3_get_column_values import get_column_values


FILENAME = "Marketing_Spend.csv"


def get_min_ofline_spend(filename: str) -> Union[int, float]:
    ofline_spend_values = get_column_values(filename, "Offline Spend")

    min_value = ofline_spend_values[0]
    for current_value in ofline_spend_values:
        if current_value < min_value:
            min_value = current_value

    return min_value


if __name__ == "__main__":
    print(get_min_ofline_spend(FILENAME))
