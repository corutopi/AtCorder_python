# 解説を参考に作成
# https://atcoder.jp/contests/abc112/submissions/16922570 を参考に作成
# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, xyh):
    xyh.sort(reverse=True, key=lambda x: x[2])
    for X in range(101):
        for Y in range(101):
            H = xyh[0][2] + abs(X - xyh[0][0]) + abs(Y - xyh[0][1])
            for x, y, h in xyh:
                if h != max(0, H - abs(X - x) - abs(Y - y)):
                    break
            else:
                print(X, Y, H)
                return


if __name__ == '__main__':
    N = int(input())
    xyh = [[int(i) for i in input().split()] for _ in range(N)]
    solve(N, xyh)

    # # test
    # from random import randint
    # from func import random_str
    # solve()
