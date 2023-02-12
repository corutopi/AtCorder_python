# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, F, P):
    ans = - 10 ** 18
    for n in range(1, 2 ** 10):
        tmp_ans = 0
        tmp_n = [n >> m & 1 for m in range(10)]
        for i in range(N):
            ci = 0
            for jk in range(10):
                if tmp_n[jk] == F[i][jk] == 1:
                    ci += 1
            tmp_ans += P[i][ci]
        ans = max(ans, tmp_ans)
    print(ans)


if __name__ == '__main__':
    # S = input()
    N = int(input())
    F = [[int(i) for i in input().split()] for _ in range(N)]
    P = [[int(i) for i in input().split()] for _ in range(N)]
    solve(N, F, P)

    # # test
    # from random import randint
    # from func import random_str, random_ints
    # solve()
