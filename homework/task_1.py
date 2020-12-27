class Animal:
    @staticmethod
    def eat():
        print('Im eating')

    @staticmethod
    def drink():
        print('Im drinking')

    @staticmethod
    def move():
        print('Im moving')


class Butterfly(Animal):
    @staticmethod
    def move():
        print('I can move and fly')

    @staticmethod
    def fly():
        print('Im flying')


class Dog(Animal):
    @staticmethod
    def run():
        print('Im running')

    @staticmethod
    def bark():
        print('Woof')


class Frog(Animal):
    @staticmethod
    def swim():
        print('Im swimming')

    @staticmethod
    def hunt():
        print('Im hunting')


class Monkey(Animal):
    @staticmethod
    def climb():
        print('Im climb a tree')

    @staticmethod
    def sleep():
        print('Zzz...')


class Spider(Animal):
    @staticmethod
    def make_webs():
        print('Im making webs')

    @staticmethod
    def bite():
        print('Im biting someone')
