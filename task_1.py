class OnlineSalesRegisterCollector:
    def __init__(self):
        self.__name_items = []
        self.__number_items = 0
        self.__item_price = {'чипсы': 50, 'кола': 100, 'печенье': 45, 'молоко': 55, 'кефир': 70}
        self.__tax_rate = {'чипсы': 20, 'кола': 20, 'печенье': 20, 'молоко': 10, 'кефир': 10}

    @property
    def name_items(self):
        return self.__name_items

    @property
    def number_items(self):
        return self.__number_items

    def add_item_to_cheque(self, name):
        if len(name) > 40 or len(name) == 0:
            raise ValueError('Нельзя добавить товар, если в его названии нет символов или их больше 40')
        if name not in self.__item_price:
            raise NameError('Позиция отсутствует в товарном справочнике')
        self.__name_items.append(name)
        self.__number_items += 1

    def delete_item_from_check(self, name):
        if name not in self.__name_items:
            raise NameError('Позиция отсутствует в чеке')
        self.__name_items.remove(name)
        self.__number_items -= 1

    def check_amount(self):
        total = []
        for item in self.__name_items:
            if item in self.__item_price:
                total.append(self.__item_price[item])
        if len(self.__name_items) > 10:
            discount = sum(total) * 0.1
            total_with_discount = sum(total) - discount
            return total_with_discount
        return sum(total)

    def twenty_percent_tax_calculation(self):
        twenty_percent_tax = []
        for item in self.__name_items:
            if item in self.__tax_rate and self.__tax_rate[item] == 20:
                twenty_percent_tax.append(item)
        total = []
        for item in twenty_percent_tax:
            if item in self.__item_price:
                total.append(self.__item_price[item])
        total_sum = sum(total)
        if len(self.__name_items) > 10:
            total_sum *= 0.9

        return total_sum * 0.2

    def ten_percent_tax_calculation(self):
        ten_percent_tax = []
        for item in self.__name_items:
            if item in self.__tax_rate and self.__tax_rate[item] == 10:
                ten_percent_tax.append(item)
        total = []
        for item in ten_percent_tax:
            if item in self.__item_price:
                total.append(self.__item_price[item])
        total_sum = sum(total)
        if len(self.__name_items) > 10:
            total_sum *= 0.9

        return total_sum * 0.1

    def total_tax(self):
        total_nds = self.twenty_percent_tax_calculation() + self.ten_percent_tax_calculation()
        return total_nds

    @staticmethod
    def get_telephone_number(telephone_number):
        if telephone_number % 1 != 0:
            raise ValueError('Необходимо ввести цифры')
        if len(str(telephone_number)) > 10:
            raise ValueError('Необходимо ввести 10 цифр после "+7"')
        return f'+7{telephone_number}'


online = OnlineSalesRegisterCollector()
online.add_item_to_cheque('кола')
online.add_item_to_cheque('чипсы')
online.add_item_to_cheque('молоко')
print(online.check_amount())
print(online.twenty_percent_tax_calculation())
print(online.ten_percent_tax_calculation())
print(online.total_tax())
print(online.get_telephone_number(9466664564))
