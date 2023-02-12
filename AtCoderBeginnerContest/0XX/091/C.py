# 解説を参考に作成
# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, AB, CD):
    pair_flg_AB = [0] * N
    AB.sort(key=lambda x: x[1], reverse=True)
    CD.sort()
    ans = 0
    for i in range(N):
        c, d = CD[i]
        for j in range(N):
            if pair_flg_AB[j] == 1:
                continue
            a, b = AB[j]
            if a < c and b < d:
                ans += 1
                pair_flg_AB[j] = 1
                break
    print(ans)


if __name__ == '__main__':
    N = int(input())
    AB = [[int(i) for i in input().split()] for _ in range(N)]
    CD = [[int(i) for i in input().split()] for _ in range(N)]
    solve(N, AB, CD)

    # # test
    # from random import randint
    # from func import random_str
    # solve()
