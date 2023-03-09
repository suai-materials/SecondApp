from random import randrange
from typing import List


def my_random_list(n: int) -> List[int]:
    """Генерация списка со случайными числами"""
    return [randrange(5, 12 * 100) for i in range(n)]


if __name__ == '__main__':
    print(my_random_list(22))