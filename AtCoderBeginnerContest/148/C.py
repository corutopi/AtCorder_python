# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect


def gcd(a, b):
    """最大公約数"""
    a, b = (a, b) if a >= b else (b, a)
    if b == 0:
        return a
    return gcd(b, a % b)


def lcm(a, b):
    """最小公倍数"""
    # from math import gcd
    return (a * b) // gcd(a, b)


# from decorator import stop_watch
#
#
# @stop_watch
def solve(A, B):
    print(lcm(A, B))


if __name__ == '__main__':
    A, B = map(int, input().split())
    solve(A, B)
