from kr import Store
from kr import Product
from kr import Customer
my_store = Store('Magnit')
my_customer_1 = Customer('Maga', my_store)
my_customer_2 = Customer('Petya', my_store)
my_product_1 = Product('Bread', 100)
my_product_2 = Product('Pepper', 200)
my_product_3 = Product('Vodka', 500)
my_store.__add__(my_product_1, my_product_1.get_price())
my_store.__add__(my_product_2, my_product_2.get_price())
my_store.__add__(my_product_3, my_product_3.get_price())
my_customer_1.buy(my_product_3, my_product_3.get_price())
my_customer_2.buy(my_product_2, my_product_2.get_price())
my_customer_1.returning(my_product_3, my_product_3.get_price())
print('Магазин:')
my_store.show()
print('Первый покупатель:')
my_customer_1.show()
print('Второй покупатель:')
my_customer_2.show()