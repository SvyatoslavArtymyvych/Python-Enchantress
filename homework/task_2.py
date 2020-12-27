# Guitar(aggregation)
class Music:
    def __init__(self, name, genre):
        self.name = name
        self.genre = genre


class Guitar:
    def __init__(self, music):
        self.music = music

    def play_music(self):
        print(f'Im playing \'{self.music.name}\'({self.music.genre})')


print('--- Aggregation ---')
music_1 = Music('We Will Rock You', 'rock')
guitar_1 = Guitar(music_1)
guitar_1.play_music()
print('\n')


# Laptop(composition)
class Disk:
    def __init__(self, disk_letter, disk_size):
        self.disk_letter = disk_letter
        self.disk_size = disk_size


class Laptop:
    def __init__(self):
        self.disks = []
        self.disks.append(Disk('C', 128))
        self.disks.append(Disk('D', 256))
        self.disks.append(Disk('E', 512))

    def show_disks(self):
        for i in self.disks:
            print(f'Disk {i.disk_letter}, size: {i.disk_size}GB')


print('--- Composition ---')
mac = Laptop()
mac.show_disks()
