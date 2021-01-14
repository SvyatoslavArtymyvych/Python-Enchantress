# 2. Create two classes: Laptop, Guitare,
#    one for composition, another one for aggregation.

# composition
class Key:
    def __init__(self, key_name):
        self.name = key_name


class Laptop:
    def __init__(self):
        self.keys = [Key(f'Key {i}') for i in range(101)]

        
# aggregation
class String:
    type:str

    def __init__(self, type):
        self.type = type


class Guitare:
    def __init__(self, strings_list):
        self.strings_list = strings_list

if __name__ == "__main__": 
    # composition
    Laptop()
    # aggregation
    strings = [String('guitar_string') for i in range(7)]
    Guitare(strings)
