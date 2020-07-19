#!/usr/bin/env python

import pytest

def multipleOf(multiple, factor):
    return (multiple % factor) == 0

def fizzbuzz(multiple):
    if (multipleOf(multiple, 3) and (multipleOf(multiple, 5))):
        return 'FizzBuzz'
    if multipleOf(multiple, 3):
        return 'Buzz'
    if multipleOf(multiple, 5):
        return 'Fizz'

def test__assertTrue():
    assert True

def test__returnFizzOnMultipleOfThree():
    assert fizzbuzz(6) == 'Buzz'

def test_returnBuzzOnMultipleOfFive():
    assert fizzbuzz(10) == 'Fizz'

def test__returnFizzBuzzOnMultipleOfThreeOrFive():
    assert fizzbuzz(15) == 'FizzBuzz'
