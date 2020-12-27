# 1. Create a class hierarchy of animals with at
#    least 5 animals that have additional methods each.

class Carnivora:
    def __init__(self):
        self.name = input('Name of animal: ')


class Canidae(Carnivora):
    lags = 4

    def run(self):
        pass


class Feliformia(Carnivora):
    pass


class Dog(Canidae):
    sound = 'gow'

    def find_drugs(self):
        pass


class Wolf(Canidae):

    def hunt_deer(self):
        pass


class Fox(Canidae):

    def hunt_birds(self):
        pass


class Cat(Feliformia):
    sound = 'meow'

    def destroy_sofa(self):
        pass

    def climb_tree(self):
        pass


class Lynx(Feliformia):

    def hunt_grouse(self):
        pass


# 1. Create two classes: Laptop, Guitare,
#    one for composition, another one for aggregation.

class Key:
    def __init__(self, key_name):
        self.name = key_name


class Laptop:
    def __init__(self):
        self.keys = [Key(f'Key {i}') for i in range(101)]


Laptop()


class String:
    pass


class Guitare:
    def __init__(self, strings_list):
        self.strings_list = strings_list


strings = [String() for i in range(7)]
Guitare(strings)


# 3. Create metaclass with inheritance
class MetaCheburek(type):
    def __new__(mcs, class_name, *args, **kwargs):
        print("We are created Cheburek class object")
        print(class_name)
        class_obj = super().__new__(mcs, class_name, *args, **kwargs)
        class_obj.ingredients = ['Potato, Cheese, Salad']
        return class_obj


class Cheburek(metaclass=MetaCheburek):
    pass


print('class object', Cheburek)
print('object', Cheburek())
