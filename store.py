class Store:
    class Product:
        def __init__(self, product_name, amount=1, cost=0):
            self.product_name = product_name
            self.amount = amount
            self.cost = cost

        def __str__(self):
            return f'\nНаименование: {self.product_name[0].upper()+self.product_name[1:]}' \
                   f'\nКолличество: {self.amount}' \
                   f'\nСтоимость {self.cost} грн. '

        def __eq__(self, other):
            return self.product_name == other

    def __init__(self):
        self.products = []  # Сдесь будут храниться все товары в магазине
        self.__iter_pos = -1

    def add_new_product(self, name, amount=1, cost=0):
        """Добавить новый товар в магазин. Есть он уже есть в магазине - увеличиваем его кол-во."""

        new_item = self.Product(name.lower(), amount, cost)  # Создаем новый товар

        for i in self.products:  # Ищем совпадения по магазину
            if i == new_item:
                i.amount += new_item.amount  # увеличиваем колличество товара, если найдены совпадения
                break
        else:
            self.products.append(new_item)  # Если нет совпадений - добавляем новый товар в магазин

    def edit_product(self, product_name):
        """Метод позволяет редактировать товар на выбор."""
        for i in self.products:  # Ищем указаную позицию в магазине.
            if i == product_name.lower():
                print('\nПозиция найдена!\nИнфо:', i, end='')
                action = input('Список команд:\n-редактирование колличества: 1'
                               '\n-Редактирование стоимости: 2\n>>>')
                if action not in ('1', '2'):
                    return print('Ошибка ввода.')
                try:
                    if action == str(1):
                        i.amount = int(input('Новое кол-во: '))

                    elif action == str(2):
                        i.cost = float(input('Новая цена: '))
                except ValueError:
                    return print('Ошибка: <Неверное значение>')
                else:
                    print('Информация обновлена.')

    def remove_product(self, p_name):
        """Удаляем товар по наименованию"""
        # Ищем совпадения:
        coincidences = False
        for i in self.products:
            if i == p_name.lower():
                self.products.remove(i)  # Удаляем найденый товар из магазина.
                coincidences = True
        else:
            #  Информируем пользователя об результате операции.
            if coincidences:
                print(f'"{p_name}" удалён из списка товаров.')
            elif not coincidences:
                print('Совпадения не найдены.')

    def __len__(self):
        return len(self.products)

    def __str__(self):
        return '\nТовары в магазине:\n'\
               + '\n'.join([f'№{self.products.index(i)+1}' + str(i) + '\n' for i in self.products])

    def __getitem__(self, item):
        return self.products[item]

    def __next__(self):
        self.__iter_pos += 1
        if self.__iter_pos >= len(self):
            self.__iter_pos = -1
            raise StopIteration
        return self.products[self.__iter_pos]

    def __iter__(self):
        return self



