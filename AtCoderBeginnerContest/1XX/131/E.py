# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
inf = float('inf')
mod = 10 ** 9 + 7

# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, K):
    if (N - 1) * (N - 2) // 2 < K:
        print(-1)
        return
    M = 0
    graph = []
    for i in range(1, N):
        graph.append([i, N])
        M += 1
    dst2_num = (N - 1) * (N - 2) // 2
    for i in range(1, N - 1):
        for j in range(i + 1, N):
            if dst2_num == K:
                break
            graph.append([i, j])
            M += 1
            dst2_num -= 1
    print(M)
    [print(' '.join([str(gg) for gg in g])) for g in graph]


if __name__ == '__main__':
    N, K = map(int, input().split())
    solve(N, K)

    # # test
    # from random import randint
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
