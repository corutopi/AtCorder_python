# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
from collections import deque


# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, M, uvc):
    tree_map = [[] for _ in range(N + 1)]
    for u, v, c in uvc:
        tree_map[u].append([v, c])
        tree_map[v].append([u, c])
    # [print(t) for t in tree_map]
    ans = [0] * (N + 1)
    visited = [False] * (N + 1)
    visited[1] = True
    ans[1] = 1
    dq = deque([1])
    while dq:
        now = dq.popleft()
        for child, c in tree_map[now]:
            if visited[child]:
                continue
            visited[child] = True
            if c == ans[now]:
                ans[child] = c % N + 1
            else:
                ans[child] = c
            dq.append(child)
    [print(i) for i in ans[1:]]


if __name__ == '__main__':
    N, M = map(int, input().split())
    uvc = [[int(i) for i in input().split()] for _ in range(M)]
    solve(N, M, uvc)

    # # test
    # from random import randint
    # from func import random_str, random_ints
    #
    # N = 4
    # M = 2 * N
    #
    #
    # def trial():
    #     a, b = 0, 0
    #     while a == b:
    #         a, b = randint(1, N), randint(1, N)
    #     return a, b, randint(1, N)
    #
    # cnt = 0
    # while True:
    #     uvc = [[i, i % N + 1, randint(1, N)] for i in range(1, N + 1)] + \
    #           [trial() for _ in range(randint(0, N))]
    #     solve(N, M, uvc)
    #     cnt += 1
    #     # if cnt % 10 == 0:
    #     #     print(cnt)
