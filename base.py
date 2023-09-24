#Сортировочный алгоритм - поиск выборкой
def selection_sort(array_sales, array_name):
    for target in range(len(array_sales)):
        min_index = target

        for index in range(target + 1, len(array_sales)):
            if array_sales[index] < array_sales[min_index]:
                min_index = index

        if min_index != target:
            array_sales[target], array_sales[min_index] = array_sales[min_index], array_sales[target]
            array_name[target], array_name[min_index] = array_name[min_index], array_name[target]

    return array_sales, array_name


#Функция по открытию файла
def open_file(filename):
    try:
        with open(filename, encoding= "ANSI") as file:
            array = file.readlines()
            array = list(map(lambda x: x.strip().split(";"), array))
            return array

    except FileNotFoundError:
        print("Ошибка - Файл не найден")

    except Exception as e:
        print(f"Ошибка - {e}")


#Функция по созданию хэш-таблицы
def hash_table(file):
    table = {}
    pillars = file.pop(0)
    for order in file:
        num = int(order.pop(0))
        table[num] = {}
        table[num]["date"] = order[0]
        table[num]["name"] = order[1]
        table[num]["category"] = order[2]
        table[num]["sales"] = int(order[3])
        table[num]["price"] = int(order[4])
        table[num]["all_price"] = int(order[5])

    return table


#Поисковый алгоритм - бинарный поиск
def binary_search(array, item):
    high = len(array) - 1
    low = 0

    while low <= high:

        mid = int((low + high) / 2)
        guess = array[mid]

        if item == guess:
            return mid
        elif item < guess:
            high = mid - 1
        else:
            low = mid + 1

    return None

