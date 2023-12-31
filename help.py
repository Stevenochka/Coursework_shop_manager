from base import *
from tabulate import tabulate
import matplotlib.pyplot as plt
from sys import stdin


class Shop_helper:

    #Инициализация и создание таблицы данных
    def __init__(self, file):
        self.table = hash_table(open_file(file))


    #Вспомогательная функция - просмотри хэш-таблицы
    def info(self):
        for item in self.table.items():
            print(item)


    #Вспомогательная функция - для подсчета общей выручки
    def __all_money(self):
        money = 0
        for num in self.table.keys():
            money += self.table[num]["all_price"]

        return money


    #Подсчет общей выручки
    def all_money(self):
        return f"Общая выручка магазина составила {self.__all_money()} руб."


    #Поиск товара с наибольшим кол-вом продаж
    def most_sales(self):
        sales = []
        names = []

        for key in self.table.keys():
            sales.append(self.table[key]["sales"])
            names.append(self.table[key]["name"])

        selection_sort(sales, names)

        if sales.count(sales[-1]) == 1:
            return f"Наибольший по кол-ву продаж товар {names[-1]} - он был продан ровно {sales[-1]} раз."
        else:
            return f"Наибольшие по кол-ву продаж товары {', '.join(names[-sales.count(sales[-1]):])} - они были проданы ровно {sales[-sales.count(sales[-1])]} раз."


    #Поиск товара с наибольшей выручкой
    def most_all_price(self):
        all_price = []
        names = []

        for key in self.table.keys():
            all_price.append(self.table[key]["all_price"])
            names.append(self.table[key]["name"])

        selection_sort(all_price, names)

        if all_price.count(all_price[-1]) == 1:
            return f"Наибольший по выручке товар {names[-1]} - его выручка составила {all_price[-1]} руб."
        else:
            return f"Наибольшие по выручке товары {names[-all_price.count(all_price[-1]):]} - их выручка составила {all_price[-all_price.count(all_price[-1])]} руб."


    #Вспомогательная функция - подсчет процентого содержания выручки от общей выручки
    def percentages(self, price):
        return round((price/self.__all_money()) * 100, 3)


    #Вспомогательная функция - отчёт о выручке магазина
    def __report_of_gain(self):
        report = []
        for key in self.table.keys():
            product = [self.table[key]["name"], str(self.table[key]["sales"]),
                       str(self.table[key]["all_price"]), self.percentages(self.table[key]["all_price"])]
            report.append(product)

        report.sort(key= lambda x: -x[-1])

        return report



    #Отчёт о выручке магазина
    def report_of_gain(self):
        print(f"Отчёт об общей выручке магазина - {self.all_money()}")
        print(tabulate(self.__report_of_gain(), headers=['Товар', 'Кол-во продаж', 'Выручка, руб',
                                                         'Процент от общей выручки, %']))

    #Функция по реализации диаграммы
    def diagram(self):
        names = [self.table[key]["name"] for key in self.table.keys()]
        data = [self.percentages(self.table[key]["all_price"]) for key in self.table.keys()]
        bubble_sort(data, 1)
        plt.title("Отчет об выручке магазина")
        plt.pie(data, labels= None, autopct='%1.1f%%')
        plt.axis('equal')
        plt.legend(labels=names, loc= 'center right')
        plt.show()


    #Функция поиска товара по индексу
    def search_by_index(self, index):
        indexes = [i for i in self.table.keys()]
        bubble_sort(indexes)
        if binary_search(indexes, index):
            print(f'Данный товар присутствует в базе данных')
            print("Хотите просмотреть информацию? (Да/нет)")
            answear = stdin.read().strip("\n")
            if answear == "Да" or answear == 'да':
                print(self.table[index])
        else:
            print(f"Товар не найден в базе данных")


    #Функция отслеживающая кол-во продаж товара такого-то производителя
    def search_productmaker(self, maker):
        count = 0
        for key in self.table.keys():
            if len(knut_moris_prat(self.table[key]["name"], maker)) > 0:
                count += 1

        if count > 0:
            print(f"Магазин за все время продал продукцию {maker} в таком количистве - {count}")
        else:
            print(f"Машазин не продавал продукт от производителя {maker}")


'''
    #Старая реализация отчета
    def report_of_gain(self):
        print(f"Отчёт об общей выручке магазина - {self.all_money()}")
        print("Товар --- Кол-во продаж --- Выручка --- Процент от общей выручки")
        for product in self.__report_of_gain():
            product[-1] = str(product[-1]) + " % "
            print(" --- ".join(product))
'''



