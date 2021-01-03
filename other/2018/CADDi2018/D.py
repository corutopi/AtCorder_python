# 解説を参考に作成
# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, a):
    print('second' if all([ai % 2 == 0 for ai in a]) else 'first')


if __name__ == '__main__':
    # S = input()
    N = int(input())
    a = [int(input()) for _ in range(N)]
    solve(N, a)

    # # test
    # from random import randint
    # from func import random_str, random_ints
    # solve()
