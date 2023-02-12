# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
mod = 10 ** 9 + 7

def cmb(n, r):
    """組み合わせ"""
    import math
    if n < r:
        return 0
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

# from decorator import stop_watch
#
#
# @stop_watch
def solve(L):
    print(cmb(L - 1, 11))


if __name__ == '__main__':
    L = int(input())
    solve(L)

    # # test
    # from random import randint
    # from func import random_str, random_ints
    # solve()
