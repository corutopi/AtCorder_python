# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# from decorator import stop_watch
#
#
# @stop_watch
def solve(x):
    if x < 0:
        x = 0
    print(x)


if __name__ == '__main__':
    x = int(input())
    solve(x)

    # # test
    # from random import randint
    # from func import random_str, random_ints
    # solve()
