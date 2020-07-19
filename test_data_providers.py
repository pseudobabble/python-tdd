#!/usr/bin/env python
import pytest
from pytest import fixture, mark

@fixture(params=[str.lower, str.upper, str.capitalize])
def my_fixture(request):
    return request.param


def test__a_test(my_fixture):
    print(my_fixture('\nTesting something'))


def is_prime(n):
    return all([(n % j) for j in range(2, int(n/2)+1)]) and n > 1

@mark.parametrize('number, expected_value', [(2, True), (3, True), (4, False), (5, True)])
def test__is_prime(number, expected_value):
    assert is_prime(number) == expected_value
