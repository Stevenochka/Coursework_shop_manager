from help import *

def main():
    file = "table.csv"
    table = Shop_helper(file)
    table.report_of_gain()
    print()
    print(table.most_all_price())
    print(table.most_sales())


if __name__ == '__main__':

    try:
        print('Программа начала работу')
        print()
        main()

    except KeyboardInterrupt:
        pass

    finally:
        print("\nПрограмма завершила работу")
