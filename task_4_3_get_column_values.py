"""
Аннотация типов
Методы списка index, append
Метод split как отдельная функция (принцип DRY)
"""

FILENAME = "Marketing_Spend.csv"


def get_column_values(filename, column):  # todo добавить аннотацию типов
    """Вернуть список значений указанного столбца"""
    with open(filename) as f:
        # todo считать строку со столбцами и разбить их

        # todo получить индекс искомого столбца
        
        # todo считать все значения столбца в список
        ...


if __name__ == "__main__":
    print(get_column_values(FILENAME, "Offline Spend"))
