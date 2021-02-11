from functools import lru_cache
number = int(input('Введите число: '))


# @lru_cache(maxsize=100, typed=False)
def recursion(number):

    if number == 1:
        return number
    else:
        return number*recursion(number-1)


print(recursion(number))
