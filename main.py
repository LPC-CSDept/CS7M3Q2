import random


def getSum(numbers, n):
    """
    ########################################
    Code Your Program here
    ########################################
    """


def main():
    numbers = [3, 8, 9, 6, 5]
    print(numbers)
    ret = getSum(numbers, 3)
    print(f'Your return value: {ret}')

    numbers = [1, 2, 3, 4, 5]
    print(numbers)
    ret = getSum(numbers, 3)
    print(f'Your return value: {ret}')

    numbers = [5, 4, 3, 2, 1]
    print(numbers)
    ret = getSum(numbers, 5)
    print(f'Your return value: {ret}')

    numbers = [5, 4, 3, 2, 1]
    print(numbers)
    ret = getSum(numbers, 1)
    print(f'Your return value: {ret}')

    numbers = [random.randint(-50, 50) for _ in range(10)]
    print(numbers)
    ret = getSum(numbers, 5)
    print(f'Your return value: {ret}')


if __name__ == '__main__':
    main()
