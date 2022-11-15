class Student:
    def __init__(self, name, group):
        print('init', name)
        self.name = name
        self.group = group

    def __new__(cls, *args, **kwargs):
        print('new')
        return super(Student, cls).__new__(cls)

    def __del__(self):
        print(self.name, 'is deleted')

    def introduce(self):
        print(f'Hi, I am {self.name} from group {self.group}')

    @staticmethod
    def say_hi(name):
        print('Hi,', name)

new_group = '11-250'
a = Student('Izida', new_group)
b = Student('Kate', '11-210')

class Collection:
    def __init__(self, list):
        self.list = list

    def __len__(self):
        return len(self.list)

list = ['Hi', 'Hello']
print(len(list))
collection = Collection(list)

print(len(collection))