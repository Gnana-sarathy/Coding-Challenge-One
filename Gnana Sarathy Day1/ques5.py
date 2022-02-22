def pattern(n):
    space = n-1
    for line in range(1, n + 1):
        print(' ' * space, end='')
        space -= 1
        c = 1
        for i in range(1, line + 1):
            print(c, end=" ")
            c = int(c * (line - i) / i)
        print()


pattern(8)
