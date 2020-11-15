# 解説を参考に作成
# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# from decorator import stop_watch
#
#
# @stop_watch
def solve(H, W, A, B):
    for h in range(H):
        if h < B:
            print('0' * A + '1' * (W - A))
        else:
            print('1' * A + '0' * (W - A))


if __name__ == '__main__':
    H, W, A, B = map(int, input().split())
    solve(H, W, A, B)

    # # test
    # from random import randint
    # from func import random_str, random_ints
    # solve()
