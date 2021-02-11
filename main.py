number = int(input('Введите число: '))


def loop(number):
    answer = 1

    for i in range(1, number+1):
        answer *= i

    return answer


print(loop(number))
