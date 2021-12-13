FILENAME = "Marketing_Spend.csv"


class MarketingSpend:
    def __init__(self, filename, separate_value=","):
        self.filename = filename
        self.separate_value = separate_value

        self.columns_list = self.get_columns_list()

        self.list_dicts = []
        self.init_list_dicts()

    def get_columns_list(self):
        with open(self.filename) as f:
            return f.readline().split(self.separate_value)

    def init_list_dicts(self):
        with open(self.filename) as f:
            self.columns_list = f.readline().split(self.separate_value)
            for line in f:
                row_values = line.split(self.separate_value)
                row_dict = {}
                for index, column in enumerate(self.columns_list):
                    row_dict[column] = row_values[index]
                self.list_dicts.append(row_dict)

    def print_list_dicts(self):
        print(self.list_dicts)


if __name__ == "__main__":
    marketing_spend = MarketingSpend(FILENAME)
    print(marketing_spend.columns_list)

    marketing_spend.print_list_dicts()
