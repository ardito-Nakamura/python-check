import json


def raise_exception_1():
    """ValueError"""
    int("a")


def raise_exception_2():
    """ZeroDivisionError"""
    1/0


def raise_exception_3():
    """KeyError"""
    dict_1 = dict(hoge=1)
    dict_1["fuga"]


def raise_exception_4():
    """TypeError"""
    "a" + 1
    # raise_exception_1(1)
    # hoge = 1
    # hoge()


def raise_exception_5():
    """AttributeError"""
    str.hoge()


def raise_exception_6():
    """SyntaxError"""

    # raise SyntaxError
