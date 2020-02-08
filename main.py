import random
from functools import reduce
def list_of_names(list1, n):
    list2 = []
    for i in range(n):
        a = random.choice(list1)
        list2.append(a)
    print(list2)
names = ['Andrew', 'Anastasiya', 'Anton', 'Sergey', 'Dima', 'Kate', 'Tatyana', 'Evgeniy', 'Maria', 'Svetlana', 'Artem', 'Igor', 'Ilya', 'Aleksey', 'Aleksandr', 'Juliya', 'Daniil', 'Konstantin', 'Kristina', 'Angelina']
list_of_names(names, 100)
