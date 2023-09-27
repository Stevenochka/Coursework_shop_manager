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
            return guess
        elif item < guess:
            high = mid - 1
        else:
            low = mid + 1

    return None


#Алгоритм сортировки - сортировка пузыркем (обменом)
def bubble_sort(array, flag=0):
    if flag == 0:
        for border in range(len(array) - 1):
            for index in range(len(array) - 1 - border):
                if array[index] > array[index + 1]:
                    array[index], array[index + 1] = array[index + 1], array[index]

        return array

    elif flag == 1:
        for border in range(len(array) - 1):
            for index in range(len(array) - 1 - border):
                if array[index] < array[index + 1]:
                    array[index], array[index + 1] = array[index + 1], array[index]

        return array

    else:
        print("Flag is incorrectly specified!")
        return False


#Функция для поиска гранци для алгоритма Кнут-Морис-прат
def find_borders(fragment):
    lenght = len(fragment)
    b = (lenght + 1) * [0]
    liters = 0

    for end_preficks in range(1, lenght):
        while liters > 0 and fragment[liters] != fragment[end_preficks]:
            liters = b[liters]
        if fragment[liters] == fragment[end_preficks]:
            liters += 1
        b[end_preficks + 1] = liters

    return b


#Алгоритм поиска строки - алгоритм кнут-мориса-прата
def knut_moris_prat(text, fragment):
    b = find_borders(fragment)
    queue = []
    lenght_text = len(text)
    lenght_fragment = len(fragment)
    liters = 0

    for element in range(lenght_text):
        while liters > 0 and fragment[liters] != text[element]:
            liters = b[liters]

        if fragment[liters] == text[element]:
            liters += 1

        if liters == lenght_fragment:
            queue.append(element - liters + 1)
            liters = b[liters]

    return queue

