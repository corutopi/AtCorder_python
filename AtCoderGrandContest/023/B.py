# 解説を参考に作成
# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, S):
    ans = 0

    for k in range(N):
        a, b = 0, k
        flg = True
        for i in range(N):
            for j in range(N):
                if S[(i + a) % N][(j + b) % N] != S[(j + a) % N][(i + b) % N]:
                    flg = False
                    break
            if flg is False:
                break
        if flg:
            ans += N
    print(ans)


if __name__ == '__main__':
    # S = input()
    N = int(input())
    S = [input() for _ in range(N)]
    solve(N, S)

    # # test
    # from random import randint
    # from func import random_str, random_ints
    # N = 300
    # S = ['a' * N for _ in range(N)]
    # solve(N, S)
