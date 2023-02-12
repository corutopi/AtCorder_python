# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
from collections import deque
# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, M, AB):
    ans = 0
    for i in range(M):
        b_map = [[] for _ in range(N + 1)]
        for j in range(M):
            if i == j:
                continue
            a, b = AB[j]
            b_map[a].append(b)
            b_map[b].append(a)
        check = [True] + [False] * N
        dq = deque([1])
        while dq:
            tmp = dq.pop()
            check[tmp] = True
            for bm in b_map[tmp]:
                if check[bm]: continue
                dq.append(bm)
        if not all(check):
            ans += 1
    print(ans)


if __name__ == '__main__':
    N, M = map(int, input().split())
    AB = [[int(i) for i in input().split()] for _ in range(M)]
    solve(N, M, AB)

    # # test
    # from random import randint
    # from func import random_str, random_ints
    # solve()
