import math


def solve():
    K = int(input())
    sum = 0
    for a in range(1, K + 1):
        for b in range(1, K + 1):
            ab = math.gcd(a, b)
            for c in range(1, K + 1):
                sum += math.gcd(ab, c)
                pass
    print(sum)


if __name__ == '__main__':
    solve()