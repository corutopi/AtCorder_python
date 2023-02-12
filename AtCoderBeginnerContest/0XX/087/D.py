# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
from collections import deque
# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, M, LRD):
    inf = 10 ** 18
    tree = [[] for _ in range(N + 1)]
    for l, r, d in LRD:
        tree[l].append(['r', r, d])
        tree[r].append(['l', l, d])

    ans = 'Yes'
    position = [inf] * (N + 1)
    for i in range(1, N + 1):
        if position[i] != inf:
            continue
        position[i] = 0
        dq = deque([i])
        while dq:
            now = dq.popleft()
            p = position[now]
            for whc, nxt, dst in tree[now]:
                if position[nxt] == inf:
                    position[nxt] = p + dst if whc == 'r' else p - dst
                    dq.append(nxt)
                else:
                    np = position[nxt]
                    if (np - p if whc == 'r' else p - np) != dst:
                        ans = 'No'
                        break
            if ans == 'No':
                break
        if ans == 'No':
            break
    print(ans)


if __name__ == '__main__':
    N, M = map(int, input().split())
    LRD = [[int(i) for i in input().split()] for _ in range(M)]
    solve(N, M, LRD)

    # # test
    # from random import randint
    # from func import random_str, random_ints
    #
    # N, M = 10 ** 5, 2 * 10 ** 5
    # LRD = []
    # for _ in range(M):
    #     l, r = randint(1, N), randint(1, N)
    #     l, r = min(l, r), max(l, r)
    #     LRD.append([l, r, r - l])
    # solve(N, M, LRD)
