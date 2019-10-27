import math


def solve():
    N = int(input())
    rN = math.ceil(N ** 0.5)

    for i in reversed(list(range(1, rN + 1))):
        if N % i == 0:
            print(int(i - 1 + (N / i) - 1))
            break


if __name__ == '__main__':
    solve()
