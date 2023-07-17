stop = int(input())
result = 0
for a in range(4):
    print(a, end=': ')
    for b in range(2):
        result += a + b
        if result > stop:
            print('-', end=' ')
            continue
        print(result, end=' ')
    print()
