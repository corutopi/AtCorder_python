# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
from collections import deque
# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, abc, Q, K, xy):
    tree_map = [[] for _ in range(N + 1)]
    for a, b, c in abc:
        tree_map[a].append([b, c])
        tree_map[b].append([a, c])
    dist_K = [-1] * (N + 1)
    dq = deque([[K, 0]])
    while dq:
        now, dst = dq.popleft()
        dist_K[now] = dst
        for t, m in tree_map[now]:
            if dist_K[t] != -1:
                continue
            dq.append([t, dst + m])
    for x, y in xy:
        print(dist_K[x] + dist_K[y])


if __name__ == '__main__':
    N = int(input())
    abc = [[int(i) for i in input().split()] for _ in range(N - 1)]
    Q, K = map(int, input().split())
    xy = [[int(i) for i in input().split()] for _ in range(Q)]
    solve(N, abc, Q, K, xy)

    # # test
    # from random import randint
    # from func import random_str, random_ints
    # solve()
