# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# from decorator import stop_watch
#
#
# @stop_watch
def solve(a, b, c, d):
    print(a * d - b * c)


if __name__ == '__main__':
    a, b = map(int, input().split())
    c, d = map(int, input().split())
    solve(a, b, c, d)

    # # test
    # from random import randint
    # from func import random_str, random_ints
    # solve()
