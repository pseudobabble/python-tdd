#!/usr/bin/env python

from pytest import mark

from .checkout import Checkout, Item, Discount, DiscountTable

# Imagine I am a properly implemented product-discount subsystem..
discount_table = {
    'bread': Discount(3, 0.5),
    'milk': Discount(2, 0.25),
    'cheese': Discount(5, 0.6)
}


def test__create_discount():
    discount = Discount(2, 0.5)

    assert isinstance(discount, Discount)
    assert discount.number == 2
    assert discount.factor == 0.5


def test__create_item():
    item = Item(5.0, 'Ham')

    assert isinstance(item, Item)
    assert item.price == 5.0
    assert item.name == 'Ham'


class TestCheckout:

    @mark.parametrize(
        'basket, num_items_in_basket',
        [
            [[Item(2.0, 'bread'), Item(2.0, 'bread')], 2],
            [[Item(2.0, 'bread'), Item(2.0, 'bread'), Item(2.0, 'bread')], 3]
        ]
    )
    def test__createCheckout(self, basket, num_items_in_basket):
        checkout = Checkout(discount_table, basket)

        assert isinstance(checkout, Checkout)
        assert isinstance(checkout.discount_table, DiscountTable)
        assert len(checkout.basket) == num_items_in_basket

    @mark.parametrize(
        'basket, total, eligible_for_discount',
        [
            [[Item(2.0, 'bread'), Item(2.0, 'bread')], 4, True],
            [[Item(2.0, 'bread'), Item(2.0, 'bread'), Item(2.0, 'bread')], 3, True],
            [[Item(2.0, 'bread'), Item(2.0, 'bread'), Item(2.0, 'bread')], 6, False],
            [[Item(2.0, 'milk'), Item(5.0, 'bread'), Item(3.0, 'cheese')], 10, False],
            [[Item(2.0, 'milk'), Item(2.0, 'milk'), Item(2.0, 'milk')], 6, False],
            [[Item(2.0, 'milk'), Item(2.0, 'milk'), Item(2.0, 'milk')], 1.5, True]
        ]
    )
    def test__get_total(self, basket, total, eligible_for_discount):
        checkout = Checkout(discount_table, basket)
        checkout_total = checkout.get_total(eligible_for_discount)

        assert total == checkout_total
