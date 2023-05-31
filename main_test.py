import main
import io
import sys
import re
import math


def test_main_1():
    captureout = io.StringIO()
    sys.stdout = captureout
    # datastr = 'Python\n3 4 1 2 0 5'
    # sys.stdin = io.StringIO(datastr)

    sys.stdout = sys.__stdout__
    print('captured ', captureout.getvalue())
    lines = captureout.getvalue().split('\n')
    print(lines)

    numbers = [3, 8, 9, 6, 5]
    pivot = numbers[-1]
    ret = main.split(numbers)
    print(f'Your return value: {ret}')
    assert ret[1] == 5, 'It must be pivot'
    assert True == all(x for x in numbers[:1] if x < pivot)
    assert True == all(x for x in numbers[2:] if x > pivot)
    # regex_string = r'[\w,\w]*1'
    # regex_string += r'[\w,\w]*3'
    # regex_string += r'[\w,\w]*5'
    # regex_string += r'[\w,\w]*'
    # print(regex_string)
    # res = re.search(regex_string, main.evenlist)
    # assert res != none
    # print(res.group())


def test_main_2():
    numbers = [1, 2, 3, 4, 5]
    pivot = numbers[-1]
    ret = main.split(numbers)
    print(f'Your return value: {ret}')
    assert ret[4] == 5, 'It must be pivot'
    assert True == all(x for x in numbers[:4] if x < pivot)
    assert True == all(x for x in numbers[4:] if x > pivot)


def test_main_3():
    numbers = [5, 4, 3, 2, 1]
    pivot = numbers[-1]
    ret = main.split(numbers)
    print(f'Your return value: {ret}')
    assert ret[0] == 1, 'It must be pivot'
    assert True == all(x for x in numbers[:0] if x < pivot)
    assert True == all(x for x in numbers[0:] if x > pivot)
