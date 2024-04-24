#!/usr/bin/env python3

class CashRegister:
  def __init__(self,discount=0):
    self.discount = discount
    self.total = 0
    self.items = []
    self.last_item = 0

  def add_item(self, title, price, quantity=1):
    self.last_item = price * quantity
    for _ in range(quantity):
      self.items.append(title)
    self.total += price*quantity
    return self.items

  def apply_discount(self):
    if self.discount:
      self.total -= self.total * (self.discount/100)
      print(f"After the discount, the total comes to ${self.total:.0f}.")
    else:
      print("There is no discount to apply.")

  def void_last_transaction(self):
    self.total -= self.last_item
    return self.total

@property
def discount(self):
  return self._discount

@discount.setter
def discount(self,discount):
  pass