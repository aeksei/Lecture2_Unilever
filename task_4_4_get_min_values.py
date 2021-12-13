# todo импортировать функцию из прошлого


FILENAME = "Marketing_Spend.csv"


def get_min_ofline_spend(filename):  # todo добавить аннотацию типов
    ofline_spend_values = ...  # todo получить столбец со значениями

    min_value = ofline_spend_values[0]
    # todo найти минимальную сумму

    return min_value


if __name__ == "__main__":
    print(get_min_ofline_spend(FILENAME))
