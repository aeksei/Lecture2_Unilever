FILENAME = "Marketing_Spend.csv"


class MarketingSpend:
    def __init__(self):  # todo аргументы для работы с csv файлом
        # todo атрибуты экземпляра

        self.columns_list = ...  # todo с помощью метода получить список колонок

        self.list_dicts = []
        # todo инициализировать список словарей

    # todo метод для получения колонок

    # todo метод для инициализации списока словарей

    # todo метод для печати


if __name__ == "__main__":
    marketing_spend = MarketingSpend(FILENAME)
    print(marketing_spend.columns_list)

    marketing_spend.print_list_dicts()
