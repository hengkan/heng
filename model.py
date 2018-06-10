"""
some examples for tracing code
"""
from typing import Union, Callable


def f(n: int) -> int:
    """
    Return g(n + 1)
    """
    x = 1
    x = g(n + 1)
    return x


def g(n: int) -> int:
    """
    Return h(n + 1)
    """
    x = 2
    x = h(n + 1)
    return x


def h(n: int) -> int:
    """ return n + 1
    """
    x = n + 1
    return x



def comprehension(list_:list)->list:
    list1=[x**2 for x in list_]
    return list1


def sum_list(list_: Union[list, int]) -> int:
    """
    Return list_, if it is an int, or the sum of all elements
    of list_ and its sub-lists.
    """
    if not isinstance(list_, list):
        return list_
    else:
        flat_list = [sum_list(x) for x in list_]
        return sum(flat_list)


class Parent:
    """
    Parent class...
    """
    def f(self, n: int) -> int:
        """
        Return 2 * g(n)
        """
        return 2 * self.g(n)

    def g(self, n) -> int:
        """
        Return 3 * n
        """
        return 3 * n


class Child(Parent):
    """
    Child class...
    """
    def g(self, n: int) -> int:
        """
        Return n

        Overrides Parent.g
        """
        return n


def filter_list(list_: list, predicate: Callable[[object], bool]) -> None:
    """
    Modify list_ so that it contains only elements that satisfy predicate.
    """
    temp_list = []
    while len(list_) > 0:
        if predicate(list_[0]):
            temp_list.append(list_.pop(0))
        else:
            scrap = list_.pop(0)
    list_ = temp_list
    # placeholder
    x = 'blah'


if __name__=="__main__":

    # tracing nested function calls
    x = 7
    a = f(1)
    print(a)

    # tracing list comprehension
    #comprehension([1,2,3])

    # tracing recursion
    # sum_list(1)
    # sum_list([1,2,3])
    # sum_list([1, [2,3], 4])

    # tracing Class Hierarchy
    # child = Child()

     #a =child.f(1)
    # print(a)

    # tracing Mutable data-types

