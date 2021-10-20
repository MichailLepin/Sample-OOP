class Store:
    def __init__(self, name):
        self.name = name
        self.store = []
        self.summary = 0

    def __add__(self, item, price):  # перегрузка оператора "+" на добавление в инвентарь
        self.store.append(item)
        self.summary += price

    def take_item(self, item, price):
        idx_item = self.store.index(item)
        self.summary -= price
        return self.store.pop(idx_item)

    def show(self):
        print('Название -', self.name, end="")
        print()
        for i in self.store:
            print(i.name)
        print('Количество товаров - ', self.store.__len__())
        print("Cтоимость -", self.summary, end="")
        print()


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_price(self):
        return self.price


class Customer:
    def __init__(self, name, store):
        self.name = name
        self.store = store
        self.customer = []
        self.summary = 0

    def buy(self, item, price):
        self.customer.append(self.store.take_item(item, price))
        self.summary += price

    def returning(self, item, price):
        self.store.__add__(item, price)
        self.customer.pop(self.customer.index(item))
        self.summary -= price

    def show(self):
        print('Имя -', self.name, end="")
        print()
        for i in self.customer:
            print(i.name)
        print('Количество товаров - ', self.customer.__len__())
        print("Cтоимость -", self.summary, end="")
        print()
