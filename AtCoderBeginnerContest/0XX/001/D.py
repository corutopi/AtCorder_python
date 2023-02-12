# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# import string
# from math import ceil, floor


N = int(input())
time_pod = [[0, 0] for _ in range((60 // 5) * 24 + 1)]
for _ in range(N):
    s, e = map(int, input().split('-'))
    s = s - s % 5
    e = e + (5 - e % 5 if e % 5 > 0 else 0)
    time_pod[s // 100 * 12 + s % 100 // 5][0] += 1
    time_pod[e // 100 * 12 + e % 100 // 5][1] += 1

tn, sp, ep = 0, -1, -1
for i in range(len(time_pod)):
    if time_pod[i][0] > 0:
        tn += time_pod[i][0]
        sp = i if sp == -1 else sp
    if time_pod[i][1] > 0:
        tn -= time_pod[i][1]
        if tn == 0:
            ep = i
            print(str(sp // 12 * 100 + sp % 12 * 5).zfill(4) + '-' +
                  str(ep // 12 * 100 + ep % 12 * 5).zfill(4))
            sp, ep = -1, -1

