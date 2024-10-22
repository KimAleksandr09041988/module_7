class Product:
    def __init__(self, name, weight, category):
        if isinstance(name, str):
            self.name = str(name)
        if isinstance(weight, int) or isinstance(weight, float):
            self.weight = float(weight)
        if isinstance(category, str):
            self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'

class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        file = open(self.__file_name, 'r')
        text = file.read()
        file.close()
        return text

    def add(self, *products):
        for item in products:
            file = open(self.__file_name, 'a')
            file.write(f'{str(item)}\n')
            file.close()

if __name__ == '__main__':
    s1 = Shop()
    p1 = Product('Potato', 50.5, 'Vegetables')
    p2 = Product('Spaghetti', 3.4, 'Groceries')
    p3 = Product('Potato', 5.5, 'Vegetables')

    print(p2) # __str__

    s1.add(p1, p2, p3)

    print(s1.get_products())