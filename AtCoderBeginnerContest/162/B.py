

def solve():
    N = int(input())
    sum = 0
    for i in range(1, N + 1):
        if i % 5 != 0 and i % 3 != 0:
            sum += i
    print(sum)


if __name__ == '__main__':
    solve()
