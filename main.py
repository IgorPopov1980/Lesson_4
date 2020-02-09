import random
def list_of_names(list1, n):
    #Функция создания списка из заданного списка имен
    #list1 - список имен
    #т - длина формируемого списка
    list2 = []
    for i in range(n):
        a = random.choice(list1)
        list2.append(a)
    return list2
names = ['Andrew', 'Anastasiya', 'Anton', 'Sergey', 'Dima', 'Kate', 'Tatyana', 'Evgeniy', 'Maria', 'Svetlana', 'Artem', 'Igor', 'Ilya', 'Aleksey', 'Aleksandr', 'Juliya', 'Daniil', 'Konstantin', 'Kristina', 'Angelina']

print(list_of_names(names, 100))
def most_pop(list_names):
    #Функция поиска самого частого имени в списке
    #list_names - список имен
    list2 = {}
    for el in list_names:
        list2[el] = list_names.count(el)
    list1 = list(list2.items())
    list1.sort(key=lambda i: i[1])
    list1.reverse()
    name1 = list1[0]
    name1 = name1[0]
    return name1

print(most_pop(list_of_names(names, 100)))

def rare_first_letter (list1):
    #Функция вывода первой буквы самого редкого имени из списка
    #list1 - список имен
    list2 = {}
    for el in list1:
        list2[el] = list1.count(el)
    list1 = list(list2.items())
    list1.sort(key = lambda i: i[1])
    name = list1[0]
    name = name[0]
    letter = name[0]
    return letter
print(rare_first_letter(list_of_names(names,100)))