number = int(input('Введите число: '))


def recursion(number):

    if number == 1:
        return number
    else:
        return number*recursion(number-1)


print(recursion(number))
