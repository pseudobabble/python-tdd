#!/usr/bin/env python
import pytest

def setup_module(module):
    print('\nSetting up module')

def teardown_module(module):
    print('\nTearing down module')

class TestClass:

    @classmethod
    def setup_class(cls):
        print('\nSetting up class')

    @classmethod
    def teardown_class(cls):
        print('\nTearing down class')

    def setup_method(self, method):
        print('\nSetting up method')

    def teardown_method(self, method):
        print('\nTearing down method')

    def test__my_method(self):
        print('\n**Executing my_method')
        assert True

def setup_function(function):
    print('\nSetting up function')

def teardown_function(function):
    print('\nTearing down function')

def test__my_function():
    print('\n**Executing my_function')
