class CinemaBar:
    @staticmethod
    def sell_product(product, customer):
        print(f"Cinema bar sold {product} to {customer.name}.")

        
cb = CinemaBar()
customer = Customer("Bob", "popcorn")
cb.sell_product(customer=customer, product=customer.food)

# 1. In directory `app` create package `cinema`. In this
# package create modules:  
#    - `bar.py` - inside this module create `CinemaBar`
#    class that describes work of cinema bar.
#    This class should have only one static method `sell_product`,
#    that takes `product` - name of the product that customer wants
#    and `customer` - `Customer` instance, that means customer.
#    The `sell_product` method sells a product to the customer and displays which product was sold and to whom.
   
   
#    ```python
#    cb = CinemaBar()
#    customer = Customer("Bob", "popcorn")
#    cb.sell_product(customer=customer, product=customer.food)
#    # Cinema bar sold popcorn to Bob.
#    ```