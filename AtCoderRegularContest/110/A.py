# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque


def lcm(a, b):
    """最小公倍数"""
    from math import gcd
    return (a * b) // gcd(a, b)


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
def solve(N):
    # ans = 1
    # for i in range(2, N + 1):
    #     ans = lcm(ans, i)
    # print(ans + 1)
    print(2329089562801)



if __name__ == '__main__':
    N = int(input())
    solve(N)

    # # test
    # from random import randint
    # from func import random_str, random_ints
    # solve()
