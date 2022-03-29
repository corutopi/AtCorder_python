# import sys
# sys.setrecursionlimit(10 ** 6)
# # for pypy
# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')

# import bisect
# from collections import deque
# import string
from math import ceil, floor

inf = float('inf')
mod = 10 ** 9 + 7
mod2 = 998244353


def gcd(a, b):
    """最大公約数"""
    a, b = (a, b) if a >= b else (b, a)
    if b == 0:
        return a
    return gcd(b, a % b)


# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, M, AC):
    AC.sort(key=lambda x: x[1])
    ans = 0
    point = N
    for i in range(M):
        a, c = AC[i]
        a %= point
        a = a if a <= point // 2 else point - a

        if a == 0:
            continue
        x = gcd(point, a)
        if x == 1:
            # if point % a != 0 or a == 1:
            ans += (point - 1) * c
            point = 0
            break

        ans += (point // x - 1) * x * c
        point = x
    print(ans if point == 0 else -1)


if __name__ == '__main__':
    # S = input()
    # N = int(input())
    N, M = map(int, input().split())
    # A = [int(i) for i in input().split()]
    # B = [int(i) for i in input().split()]
    AC = [[int(i) for i in input().split()] for _ in range(M)]
    # P = [int(input()) for _ in range(N)]
    solve(N, M, AC)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
