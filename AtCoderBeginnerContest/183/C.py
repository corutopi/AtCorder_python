# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
from collections import deque
# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, K, T):
    ans = 0
    dq = deque([[0, 0, 1]])
    while dq:
        now, time, visited = dq.pop()
        cnt = 0
        for i in range(N):
            if visited >> i & 1:
                cnt += 1
            else:
                dq.append([i, time + T[now][i], visited + (2 ** i)])
        if cnt == N:
            if K == time + T[now][0]:
                ans += 1
    print(ans)


if __name__ == '__main__':
    N, K = map(int, input().split())
    T = [[int(i) for i in input().split()] for _ in range(N)]
    solve(N, K, T)

    # # test
    # from random import randint
    # from func import random_str, random_ints
    # solve()
