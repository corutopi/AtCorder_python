# 解説を参考に作成
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
def solve(N, A):
    ma = max(A)
    tree = [set() for _ in range(ma + 1)]
    for i in range(N // 2):
        a, b = A[i], A[N - i - 1]
        if a == b: continue
        tree[a].add(b)
        tree[b].add(a)

    ans = 0
    visited = [0] * (ma + 1)
    for i in range(ma + 1):
        if visited[i] == 1: continue
        if len(tree[i]) == 0: continue
        dq = deque([i])
        ans += 1
        while dq:
            n = dq.popleft()
            visited[n] = 1
            for t in tree[n]:
                if visited[t] == 1: continue
                dq.append(t)
    print(sum(visited) - ans)


if __name__ == '__main__':
    N = int(input())
    A = [int(i) for i in input().split()]
    solve(N, A)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
