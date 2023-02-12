# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
from collections import deque
# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, M, ABs):
    f_map = [[] for _ in range(N + 1)]
    for A, B in ABs:
        f_map[A].append(B)
        f_map[B].append(A)
    group = [-1] * (N + 1)
    latest_gnum = 1
    for i in range(1, N  + 1):
        if group[i] != -1:
            continue
        group[i] = latest_gnum
        latest_gnum += 1
        dq = deque([i])
        while dq:
            n = dq.popleft()
            for f in f_map[n]:
                if group[f] != -1:
                    continue
                group[f] = group[n]
                dq.append(f)
    group_sum = [0] * latest_gnum
    for g in group[1:]:
        group_sum[g] += 1
    print(max(group_sum))


if __name__ == '__main__':
    # S = input()
    # N = int(input())
    N, M = map(int, input().split())
    ABs = [[int(i) for i in input().split()] for _ in range(M)]
    # Bs = [int(i) for i in input().split()]
    solve(N, M, ABs)
