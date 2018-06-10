""" implement tree ADT
This file is obtained from L0301 lecture and a little change is made.
"""
from typing import List, Any


class Tree:
    """
    A bare-bones Tree ADT that identifies the root with the entire tree.
    """
    def __init__(self, value: Any = None, score: int = None,
                 children: List['Tree'] = None) -> None:
        """
        Create Tree self with content value and 0 or more children
        """
        self.value = value
        self.score = score
        self.children = children.copy() if children is not None else []


if __name__ == '__main__':
    from python_ta import check_all
    check_all(config="a2_pyta.txt")
