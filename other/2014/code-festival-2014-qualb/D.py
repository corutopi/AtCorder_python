import sys
sys.setrecursionlimit(10 ** 6)
# # for pypy
# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')

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
def solve(N, H):
    tmp_list = [-1] * N
    # to left

    def dfs(now):
        # return (num of mount that can see from now, check_depth)
        if now == N - 1 or H[now] < H[now + 1]:
            tmp_list[now] = 0
            return 0, now
        see = 0
        nxt = now + 1
        while nxt < N and H[now] >= H[nxt]:
            tmp, depth = dfs(nxt)
            see += tmp + 1
            nxt = depth + 1
        tmp_list[now] = see
        return see, nxt - 1

    x = 0
    while x < N:
        _, x = dfs(x)
        x += 1
    see_left_list = tmp_list

    H.reverse()
    tmp_list = [-1] * N
    x = 0
    while x < N:
        _, x = dfs(x)
        x += 1
    see_right_list = list(reversed(tmp_list))

    for i in range(N):
        print(see_left_list[i] + see_right_list[i])


if __name__ == '__main__':
    N = int(input())
    H = [int(input()) for _ in range(N)]
    solve(N, H)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
