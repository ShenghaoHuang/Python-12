from typing import List, Dict, Set, Callable
import enum


class Parity(enum.Enum):
    ODD = 0
    EVEN = 1


def gen_list(start: int, stop: int, parity: Parity) -> List[int]:
    """
    Oh no some evil developer decided not to write docstrings. Maybe you can use the test cases to decipher
    what this method was supposed to do. Hey if you do, maybe you could do some good in this world by
    updating this here docstring to something useful.

    :param start:
    :param stop:
    :param parity:
    :return:
    """
    if parity.value == 0:
        alist = list(range(start, stop))
        rlist = [x for x in alist if x%2==1]
        return rlist
    elif parity.value == 1:
        alist = list(range(start, stop))
        rlist = [x for x in alist if x%2==0]
        return rlist


def gen_dict(start: int, stop: int, strategy: Callable) -> Dict:
    """
    Oh no some evil developer decided not to write docstrings. Maybe you can use the test cases to decipher
    what this method was supposed to do. Hey if you do, maybe you could do some good in this world by
    updating this here docstring to something useful.



    :param start:
    :param stop:
    :param strategy:
    :return:
    """
    dict = {}
    x = list(range(start, stop))

    for key in x:
        dict[key] = strategy(start)
        start += 1
    return dict


def gen_set(val_in: str) -> Set:
    """
    Oh no some evil developer decided not to write docstrings. Maybe you can use the test cases to decipher
    what this method was supposed to do. Hey if you do, maybe you could do some good in this world by
    updating this here docstring to something useful.

    :param val_in:
    :return:
    """
    aSet = set()
    alist = []

    for letter in val_in:
        if letter.isupper() == False:
            alist.append(letter.upper())
        elif val_in.isupper() == True:
            return aSet
    return set(alist)

