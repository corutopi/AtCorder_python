# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# import string
from math import ceil, floor
inf = float('inf')
mod = 10 ** 9 + 7
mod2 = 998244353

# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, A):
    ans = 0
    next_card = [0] * N
    game_num = 0
    while game_num < N * (N - 1) // 2:
        visited = [0] * N
        v_flg = 0
        for i in range(N):
            if next_card[i] == N - 1: continue
            if visited[i] == 1: continue
            j = A[i][next_card[i]]   # iが次に対戦したい人
            if next_card[j] == N - 1: continue
            if A[j][next_card[j]] == i \
                    and visited[j] == 0:
                visited[i] = 1
                visited[j] = 1
                next_card[i] += 1
                next_card[j] += 1
                game_num += 1
                v_flg = 1
        if v_flg == 0:
            print(-1)
            return
        ans += 1
    print(ans)


if __name__ == '__main__':
    N = int(input())
    A = [[int(i) - 1 for i in input().split()] for _ in range(N)]
    solve(N, A)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
