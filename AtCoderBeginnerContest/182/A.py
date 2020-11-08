# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# from decorator import stop_watch
#
#
# @stop_watch
def solve(A, B):
    print(2 * A + 100 - B)


if __name__ == '__main__':
    # S = input()
    # N = int(input())
    A, B = map(int, input().split())
    solve(A, B)

    # # test
    # from random import randint
    # from func import random_str, random_ints
    # solve()
