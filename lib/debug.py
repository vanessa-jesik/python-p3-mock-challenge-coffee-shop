#!/usr/bin/env python3
import ipdb
from classes.many_to_many import Coffee, Customer, Order

if __name__ == "__main__":
    print("HELLO! :) let's debug")

mocha = Coffee("mocha")
americano = Coffee("americano")

al = Customer("al")
jane = Customer("jane")
jane2 = Customer("jane")

order1 = Order("al", "americano", 5.0)
order2 = Order("jane", "americano", 5.0)
order3 = Order("jane", "mocha", 3.0)

ipdb.set_trace()
