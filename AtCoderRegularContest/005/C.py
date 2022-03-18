# import sys
# sys.setrecursionlimit(10 ** 6)
# # for pypy
# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
from heapq import heappush, heappop
# import bisect
# from collections import deque
# import string
from math import ceil, floor

inf = float('inf')
mod = 10 ** 9 + 7
mod2 = 998244353

# from decorator import stop_watch
#
#
# @stop_watch
def solve(H, W, C):
    sh, sw = 0, 0
    for h, w in ((h, w) for h in range(H) for w in range(W)):
        if C[h][w] == 's':
            sh, sw = h, w
            break
    shortest_map = [[inf] * W for _ in range(H)]
    shortest_map[sh][sw] = 0
    hq = [[0, sh, sw]]
    while hq:
        cost, h, w = heappop(hq)
        if shortest_map[h][w] < cost:
            continue
        if C[h][w] == 'g':
            print('YES' if cost <= 2 else 'NO')
            break
        shortest_map[h][w] = cost
        for nh, nw in ((h - 1, w), (h + 1, w), (h, w - 1), (h, w + 1)):
            if not (0 <= nh < H) or not (0 <= nw < W):
                continue
            if C[nh][nw] == '#':
                if shortest_map[nh][nw] > cost + 1:
                    shortest_map[nh][nw] = cost + 1
                    heappush(hq, [cost + 1, nh, nw])
            else:
                if shortest_map[nh][nw] > cost:
                    shortest_map[nh][nw] = cost
                    heappush(hq, [cost, nh, nw])


if __name__ == '__main__':
    H, W = map(int, input().split())
    C = [input() for _ in range(H)]
    solve(H, W, C)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    #
    # H, W = 500, 500
    # C = [random_str(W, '.#') for _ in range(H)]
    # sh, sw, gh, gw = 0, 0, H - 1, W - 1
    # while (sh == gh) and (sw == gw):
    #     sh, sw = randint(0, H), randint(0, W)
    #     gh, gw = randint(0, H), randint(0, W)
    # C[sh] = C[sh][:sw] + 's' + C[sh][sw + 1:]
    # C[gh] = C[gh][:gw] + 'g' + C[gh][gw + 1:]
    # solve(H, W, C)
