from help import *


def main():
    file = "table.csv"
    table = Shop_helper(file)
    table.report_of_gain()
    print()
    print(table.most_all_price())
    print(table.most_sales())
    print()
    table.info()
    print()
    table.search_by_index(4002)
    print()
    table.search_productmaker('Samsung')
    table.diagram()


if __name__ == '__main__':

    try:
        print('Программа начала работу')
        print()
        main()

    except KeyboardInterrupt:
        pass

    finally:
        print("\nПрограмма завершила работу")

'''
labels = ['Nokia','Samsung','Apple','Lumia']
values = [10,30,45,15]
colors = ['yellow','green','red','blue']
plt.pie(values,labels=labels,colors=colors)
plt.axis('equal')
plt.show()
'''