class Coffee:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name) >= 3 and not hasattr(self, "name"):
            self._name = name
        else:
            raise Exception

    def orders(self):
        return [order for order in Order.all if order.coffee is self]

    def customers(self):
        return list(
            set([order.customer for order in Order.all if order.coffee is self])
        )

    def num_orders(self):
        if [order for order in Order.all if order.coffee is self]:
            return len([order for order in Order.all if order.coffee is self])
        else:
            return 0

    def average_price(self):
        if [order for order in Order.all if order.coffee is self]:
            return sum(
                [order.price for order in Order.all if order.coffee is self]
            ) / len([order.price for order in Order.all if order.coffee is self])


class Customer:
    all = []

    def __init__(self, name):
        self.name = name
        Customer.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 15:
            self._name = name
        else:
            raise Exception

    def orders(self):
        return [order for order in Order.all if order.customer is self]

    def coffees(self):
        return list(
            set([order.coffee for order in Order.all if order.customer is self])
        )

    def create_order(self, coffee, price):
        return Order(self, coffee, price)

    @classmethod
    def most_aficionado(cls, coffee):
        # if not isinstance(coffee, Coffee):
        #     raise Exception
        if coffee_all_orders := [
            order for order in Order.all if order.coffee is coffee
        ]:
            return max(
                cls.all,
                key=lambda customer: sum(
                    order.price
                    for order in coffee_all_orders
                    if order.customer is customer
                ),
            )
        return None


class Order:
    all = []

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        Order.all.append(self)

    @property
    def customer(self):
        return self._customer

    @customer.setter
    def customer(self, customer):
        if isinstance(customer, Customer):
            self._customer = customer
        else:
            raise Exception

    @property
    def coffee(self):
        return self._coffee

    @coffee.setter
    def coffee(self, coffee):
        if isinstance(coffee, Coffee):
            self._coffee = coffee
        else:
            raise Exception

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        if (
            isinstance(price, float)
            and 1.0 <= price <= 10.0
            and not hasattr(self, "price")
        ):
            self._price = price
        else:
            raise Exception
