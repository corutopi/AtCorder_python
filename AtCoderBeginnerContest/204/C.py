# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
from collections import deque
# import string
from math import ceil, floor

inf = float('inf')
mod = 10 ** 9 + 7
mod2 = 998244353

# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, M, AB):
    roadmap = [[] for _ in range(N + 1)]
    for a, b in AB:
        roadmap[a].append(b)
    ans = 0
    for n in range(1, N + 1):
        goal = [0] * (N + 1)
        dq = deque([n])
        while dq:
            now = dq.popleft()
            goal[now] = 1
            for rm in roadmap[now]:
                if goal[rm] == 1: continue
                dq.append(rm)
        ans += sum(goal)
    print(ans)


if __name__ == '__main__':
    N, M = map(int, input().split())
    AB = [[int(i) for i in input().split()] for _ in range(M)]
    solve(N, M, AB)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    #
    # N, M = 2000, 2000
    # AB = tt.make_test_graph_data(N, M)
    # solve(N, M, AB)
