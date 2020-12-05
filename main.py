import store
import customer_and_card as Customer


def main():
    main_store = store.Store()
    main_store.add_new_product('Banana', 5, 30)
    main_store.add_new_product('coffee', 10, 150)
    main_store.add_new_product('car', 2, 275000)
    main_store.add_new_product('juice', 12, 45)

    customer = Customer.Customer('Nazar', 200, main_store)

    customer.add_product_to_cart('banana', 5)
    customer.add_product_to_cart('juice')
    customer.buy_from_cart()
    print(customer)
    customer.show_products_in_cart()

if __name__ == '__main__':
    main()
