def pattern1(n):
    for i in range(n):
        for j in range(i + 1):
            print('*', end='')
        print()

def pattern2(n):
    for i in range(n, 0, -1):
        for j in range(i):
            print('*', end='')
        print()

def pattern3(n):
    for i in range(n):
        for j in range(n - i - 1):
            print(' ', end='')
        for j in range(i + 1):
            print('*', end='')
        print()

def pattern4(n):
    for i in range(n):
        for j in range(n + i):
            print(' ', end='')
        for j in range(n - i):
            print('*', end='')
        print()
        for j in range(n - i):
            print('*', end='')
        print()

def pattern5(n):
    for i in range(n):
        print('*', end='')
    print()
    for i in range(n - 2):
        print('*')
    for i in range(n):
        print('*', end='')
    print()
    for i in range(n - 2):
        for j in range(n - 1):
            print(" ", end='')
        print("*", end='')
        print()
    for i in range(n):
        print('*', end='')
    print()

def pattern6(n):
    for i in range(n, 0, -2):
        for j in range((n - i) // 2):
            print(' ', end='')
        for j in range(i):
            print('*', end='')
        print()
    for i in range(2 - (n % 2), n+1, 2):
        for j in range((n - i) // 2):
            print(' ', end='')
        for j in range(i):
            print('*', end='')
        print()






pattern6(3)
pattern6(4)
