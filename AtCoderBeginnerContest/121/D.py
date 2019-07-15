"""
D - XOR World
案①:
    普通に求める

"""

import math


def solve():
    A, B = map(int, input().split())
    ans = A
    for a in range(A + 1, B + 1):
        ans ^= a
    print(bin(ans))


if __name__ == '__main__':
    solve()
