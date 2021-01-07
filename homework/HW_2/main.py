class PersonMetaClass(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Realtor(metaclass=PersonMetaClass):
    def __init__(self, name: str, houses: list, discount: int):
        self.name = name
        self.houses = houses
        self.discount = discount

    def provide_information(self):
        print(f"My name is {self.name}. Im realtor. I can sell you {len(self.houses)} houses. "
              f"I provide {self.discount}% discount")

    def provide_information_houses(self):
        print(f'{self.name} | I can sell you {len(self.houses)} houses:')
        for house in self.houses:
            house.apply_discount(self.discount)
            house.info()

    def steal_money(self, client, amount):
        client.money -= amount
        print(f'Realtor steal {amount}$')

    def sell_house(self, client):
        from random import randint

        for house in self.houses:
            house.apply_discount(self.discount)
            if client.money >= house.cost:
                if randint(0, 10) == 1:
                    self.steal_money(client, house.cost)
                else:
                    client.buy_house(house.cost)
                    break


class Person(metaclass=PersonMetaClass):
    def __init__(self, name: str, age: int, money: float, house: bool):
        self.name = name
        self.age = age
        self.money = money
        self.house = house

    def provide_information(self):
        print(f"My name is {self.name}. Im {self.age} years old. I have {self.money}$. "
              f"I{'' if self.house else ' dont'} have a house.")

    def work(self):
        self.money += 200
        print(f'{self.name} | Im working. I earned 200$. Now i have {self.money}$')

    def buy_house(self, price):
        if self.money >= price:
            self.money -= price
            self.house = True
            print(f'{self.name} | WooHoo now i have a house.')
        else:
            print(f'{self.name} | Oh... I dont have enough money. I need {price - self.money}$ more')


class House:
    def __init__(self, area: float):
        self.area = area
        self.cost = area * 15
        self.discount = 0
        self.cost_without_discount = self.cost

    def info(self):
        print(f'Area: {self.area} m². Price: {self.cost}$. Discount: {self.discount}%')

    def apply_discount(self, discount):
        self.discount = discount
        self.cost = self.cost_without_discount - (self.cost_without_discount * discount / 100)
        # print(f'New cost: {self.cost}$')


if __name__ == '__main__':
    worker = Person('Bob', 18, 50, False)
    realtor = Realtor('Max', [House(40), House(60), House(80)], 50)

    worker.provide_information()
    realtor.provide_information()
    print('')
    realtor.provide_information_houses()
    print('')

    house_1 = House(40)

    # Without realtor
    # while not worker.house:
    #     worker.work()
    #     worker.buy_house(house_1.cost)

    # With realtor
    while not worker.house:
        worker.work()
        realtor.sell_house(worker)
