import sys
sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
mod = 10 ** 9 + 7

from decorator import stop_watch


@stop_watch
def solve(N, M, uvl):
    tree_map = [[] for _ in range(N + 1)]
    for i in range(M):
        u, v, l = uvl[i]
        tree_map[u].append([v, l, i])
        tree_map[v].append([u, l, i])
    visited_top = [0] * (N + 1)
    visited_load = [0] * M
    ans = 10 ** 18

    def dfs(now, dst, now_min):
        if now == 1 and dst > 0:
            return min(now_min, dst)
        for next, load, load_num in tree_map[now]:
            if visited_load[load_num] == 1:
                continue
            if visited_top[next] == 1:
                continue
            if dst + load >= now_min:
                continue
            visited_top[next] = 1
            visited_load[load_num] = 1
            now_min = dfs(next, dst + load, now_min)
            visited_load[load_num] = 0
            visited_top[next] = 0
        return now_min

    ans = dfs(1, 0, ans)
    ans = -1 if ans == 10 ** 18 else ans
    print(ans)


if __name__ == '__main__':
    N, M = map(int, input().split())
    uvl = [[int(i) for i in input().split()] for _ in range(M)]
    solve(N, M, uvl)

    # # test
    # from random import randint
    # from func import random_str, random_ints
    # N = 200
    # M = N * (N - 1) // 2
    # uvl = []
    # for _ in range(M):
    #     u = v = 0
    #     while u == v:
    #         u = randint(1, N)
    #         v = randint(1, N)
    #     l = randint(1, 1000)
    #     uvl.append([u, v, l])
    # solve(N, M, uvl)
