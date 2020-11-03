# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, H):
    ans = 0
    up_flg = False
    down_flg = False
    s, t, u = 0, 0, 0
    for i in range(1, N):
        if H[i - 1] < H[i]:
            if down_flg:
                u = i - 1
                ans = max(ans, u - s + 1)
                up_flg = False
                down_flg = False
                s, t, u = 0, 0, 0
            if up_flg:
                continue
            else:
                up_flg = True
                s = i - 1
        if H[i - 1] > H[i]:
            down_flg = True
    u = N - 1
    ans = max(ans, u - s + 1)
    print(ans)


if __name__ == '__main__':
    # S = input()
    N = int(input())
    H = [int(input()) for _ in range(N)]
    solve(N, H)

    # # test
    # from random import randint
    # from func import random_str, random_ints
    # solve()
