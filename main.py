def encrypt(strval, indices):
    """
    ########################################
    Code Your Program here
    ########################################
    """


def main():
    strval = 'Python'
    indices = [1, 2, 3, 4, 5, 0]
    ret = encrypt(strval, indices)
    print(f'Your return value: {ret}')

    strval = 'Python'
    indices = [3, 4, 1, 2, 5, 0]
    ret = encrypt(strval, indices)
    print(f'Your return value: {ret}')

    strval = 'Python'
    indices = [0, 5, 1, 2, 3, 4]
    ret = encrypt(strval, indices)
    print(f'Your return value: {ret}')


if __name__ == '__main__':
    main()
