#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.last_transaction = 0

    def add_item(self, title, price, quantity=1):
        total_price = price * quantity
        self.total += total_price
        self.last_transaction = total_price
        for _ in range(quantity):
            self.items.append(title)

    def apply_discount(self):
        if self.discount:
            discounted_total = self.total - (self.total * self.discount / 100)
            self.total = discounted_total
            display_total = int(self.total) if self.total == int(self.total) else self.total
            print(f"After the discount, the total comes to ${display_total}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        self.total -= self.last_transaction
        self.last_transaction = 0