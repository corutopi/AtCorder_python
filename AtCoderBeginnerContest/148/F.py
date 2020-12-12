import sys
sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, u, v, AB):
    tree_map = [[] for _ in range(N + 1)]
    for a, b in AB:
        tree_map[a].append(b)
        tree_map[b].append(a)
    top_data = [[] for _ in range(N + 1)]  # parent, depth, max_depth

    def dfs(now, parent, depth):
        max_depth = depth
        for tm in tree_map[now]:
            if tm == parent:
                continue
            max_depth = max(max_depth, dfs(tm, now, depth + 1))
        top_data[now] = [parent, depth, max_depth]
        return max_depth

    dfs(v, 0, 0)

    max_p = u
    for _ in range((top_data[u][1] - 1) // 2):
        max_p = top_data[max_p][0]
    print(top_data[max_p][2] - 1)


if __name__ == '__main__':
    N, u, v = map(int, input().split())
    AB = [[int(i) for i in input().split()] for _ in range(N - 1)]
    solve(N, u, v, AB)

    # # test
    # from random import randint
    # from func import random_str, random_ints
    # solve()
