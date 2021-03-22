def loop(number):
    answer = 1

    for i in range(1, number+1):
        answer *= i

    return answer


if __name__ == "__main__":
    number = int(input('Введите число: '))
    print(loop(number))
