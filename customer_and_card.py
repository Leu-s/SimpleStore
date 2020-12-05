import copy


class ShoppingCart:
    def __init__(self, store):
        self.store = store  # Указываем какому магазину пренадлежит корзина
        self.cart = []  # Список товаров в корзине

    def add_product_to_cart(self, p_name, amount=1):
        """Добавить товар из магазина в корзину"""
        new_product = None
        amount_and_availability_check = False
        item_in_store = None
        # Проверяем есть ли такой товар в магазине
        for i in self.store:
            if i == p_name.lower():
                # Товар найдет, теперь нужно убедиться
                # нет ли его недостатка на складе
                if i.amount >= amount:
                    item_in_store = i
                    amount_and_availability_check = True
                    new_product = copy.copy(i)  # Создаем копию товара

        # Проверяем если уже такой товар у нас в корзине
        item_in_cart = False
        item_from_card = None  # Тут будет хранится товар из корзины, если таковой имеется
        for i in self.cart:
            if i == p_name.lower():
                item_in_cart = True
                item_from_card = i

        if amount_and_availability_check and not item_in_cart:
            new_product.amount = amount
            self.cart.append(new_product)
            item_in_store.amount -= amount
        elif amount_and_availability_check and item_in_cart:
            item_from_card.amount += amount
            item_in_store.amount -= amount

        # Выводим результат операции
        if amount_and_availability_check:
            print(f'"{p_name[0].upper()+p_name[1:]}" успешно добавлен в корзину в кол-ве: {amount} шт.')

        elif not amount_and_availability_check:
            print('Товар не был добавлен в корзину. Проверьте правильность наименования и колличество.')

    def remove_product_from_card(self, p_name, amount=1):
        """Возвращаем товар с корзины в магазин"""
        item_in_cart = False

        # Проверяем наличие товара в корзине
        for i in self.cart:
            if i == p_name.lower():
                # Товар найден. Проверяем кол-во
                if i.amount >= amount:
                    i.amount -= amount  # Уменьшаем кол-во товара в корзине
                    item_in_cart = True

                    # Если кол-во товара в корзине равно нулю - удаляем запись
                    if i.amount <= 0:
                        self.cart.remove(i)

        # Теперь нужно вернуть товар в магазин
        if item_in_cart:
            # Ищем наш товар в магазине
            for i in self.store:
                if i == p_name.lower():
                    i.amount += amount  # Товар найден, возвращаем товар с корзины в магазин.

        # Выводим информацию о результате операции
        if item_in_cart:
            print(f'"{p_name[0].upper() + p_name[1:].lower()}" удален из корзины.')
        elif not item_in_cart:
            print('Ошибка. Проверьте наименование товара и колличество.')

    def show_products_in_store(self):
        """Показать все товары из магазина"""
        print(self.store)

    def show_products_in_cart(self):
        """Показать все товары в корзине"""
        if self.cart:
            print('\nТовары в корзине:',
                  '\n'.join([f'\n№{self.cart.index(i) + 1}' + str(i) + '\n' for i in self.cart]))
        elif not self.cart:
            print('<Корзина пуста>')

    def cost_of_items(self):
        """Считаем кол-во товаров в корзине и его стоимость"""
        cost = 0
        amount = 0
        if self.cart:
            for i in self.cart:
                cost += i.cost * i.amount
                amount += i.amount
            else:
                return [amount, cost]
        elif not self.cart:
            return None

    def show_cost_of_items(self):
        """Показать кол-во товаров в корзине и его стоимость"""
        info = self.cost_of_items()
        if info:
            print(f'В ваше корзине есть {info[0]} товаров на сумму {info[1]} грн.')
        elif not info:
            print('Ваша корзина пуста.')


class Customer(ShoppingCart):
    def __init__(self, name, money, store):
        super().__init__(store)
        self.name = name
        self.money = money
        self.purchased_goods = []

    def buy_from_cart(self):
        """Покупаем весь товар, который находится в корзине"""
        cost_of_items = self.cost_of_items()
        if self.money >= cost_of_items[1]:
            for item in self.cart:
                self.purchased_goods.append(item)
            else:
                self.cart.clear()
                self.money -= cost_of_items[1]

    def add_money(self, amount=100):
        """Добавить денег $_$"""
        self.money += amount

    def __str__(self):
        purchase_lst = ''

        if self.purchased_goods:
            purchase_lst = "\n".join(['№'+str(self.purchased_goods.index(i)+1) + ' - '
                                      + str(i.product_name[0].upper()) +
                                      str(i.product_name[1:].lower()) for i in self.purchased_goods])
        elif not self.purchased_goods:
            purchase_lst = '<Список покупок пуст>'

        return f'Имя: {self.name}\n' \
               f'Деньги: {self.money} грн.\n' \
               f'Список покупок:\n{purchase_lst}\n'
