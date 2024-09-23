class Product():
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop():
    __file_name = 'products.txt'

    def get_products(self):
        file = open(self.__file_name, 'r')
        file.close()
        return file

    def add(self, *products):
        list_of_products = products
        print(list_of_products[0], type(list_of_products))
        for i in list_of_products:
            file = open(self.__file_name, 'r')
            if i in file:
                print(f'Продукт {i} уже есть в магазине')
                file.close()
            else:
                file.close()
                file = open(self.__file_name, 'a')
                print(i)
                file.write(str(i)+ '\n')
                file.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print('Это задание', p2)  # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
