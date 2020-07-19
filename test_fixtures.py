#!/usr/bin/env python
import pytest
from pytest import fixture, mark

def finalize():
    print('\nI clean up using REQUEST.ADDFINALIZER')


@fixture(scope='function', autouse=True)
def fixture_function():
    print('\nI help FUNCTIONS do their jobs!')
    yield
    print('\nI clean up using YIELD')


@fixture(scope='class', autouse=True)
def fixture_class():
    print('\nI help CLASSES do their jobs!')
    yield
    print('\nI clean up using YIELD')


@fixture(scope='module', autouse=True)
def fixture_module(request):
    print('\nI help MODULES do their jobs!')
    request.addfinalizer(finalize)


@fixture(scope='session', autouse=True)
def fixture_session(request):
    print('\nI help SESSIONS do their jobs!')
    request.addfinalizer(finalize)


class TestClass:

    def test__something(self):
        print('\nTesting something...')
        assert True

    def test__something_else(self):
        print('\nTesting something ELSE')
        assert True


