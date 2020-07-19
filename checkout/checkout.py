#!/usr/bin/env python

from typing import List, Dict

class Discount:

    def __init__(self, number: int, factor: float) -> None:
        self.number = number
        self.factor = factor


DiscountTable = Dict[str, Discount]


class Item:

    def __init__(self, price: float, name: str) -> None:
        self.price = price
        self.name = name


Basket = List[Item]


class Checkout:

    def __init__(self, discount_table: DiscountTable, basket: Basket) -> None:
        self.discount_table = discount_table
        self.basket = basket

    def _apply_discounts(self) -> None:
        discounted_basket = []
        discountable_product_names = self.discount_table.keys()
        for product_name in discountable_product_names:
            product_discount = self.discount_table[product_name]
            items = [item for item in self.basket if item.name == product_name]
            if len(items) >= product_discount.number:
                for item in items:
                    discounted_basket.append(
                        Item(product_discount.factor * item.price, product_name)
                    )
            else:
                discounted_basket.extend(items)
        self.basket = discounted_basket

    def get_total(self, eligible_for_discount: bool) -> float:
        if eligible_for_discount:
            self._apply_discounts()

        return sum([item.price for item in self.basket])
