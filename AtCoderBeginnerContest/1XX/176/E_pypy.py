# import sys
# sys.setrecursionlimit(10 ** 6)
import bisect
# from collections import deque
# from decorator import stop_watch
#
#
# @stop_watch
def solve(H, W, M, BOMs):
    h_count = [[0, i] for i in range(H + 1)]
    w_count = [[0, i] for i in range(W + 1)]
    bom_map_h = [[] for i in range(H + 1)]
    BOMs.sort(key=lambda x: x[1])
    for bom in BOMs:
        h_count[bom[0]][0] += 1
        w_count[bom[1]][0] += 1
        bom_map_h[bom[0]].append(bom[1])
    h_count.sort(reverse=True)
    w_count.sort(reverse=True)
    h_max = h_count[0][0]
    w_max = w_count[0][0]
    ans = h_max + w_max - 1
    flg = False
    for hc in h_count:
        if hc[0] < h_max:
            break
        for wc in w_count:
            if wc[0] < w_max:
                break
            aaa = bom_map_h[hc[1]]
            bbb = bisect.bisect_left(bom_map_h[hc[1]], wc[1])
            if len(aaa) == bbb or aaa[bbb] != wc[1]:
            # if bom_map_h[hc[1]][bisect.bisect_left(bom_map_h[hc[1]], wc[1])] != wc[1]:
            # if not wc[1] in bom_map_h[hc[1]]:
                ans = h_max + w_max
                flg = True
                break
        if flg:
            break
    print(ans)


if __name__ == '__main__':
    # S = input()
    # N = int(input())
    H, W, M = map(int, input().split())
    BOMs = [[int(i) for i in input().split()] for _ in range(M)]
    # As = [int(i) for i in input().split()]
    # Bs = [int(i) for i in input().split()]

    # import random
    # H, W = 10, 10
    # M = random.randint(1, H * W)
    # BOMs = []
    # bom_map = [[0] * W for _ in range(H)]
    # i = 0
    # while i < M:
    #     h = random.randint(1, H)
    #     w = random.randint(1, W)
    #     if bom_map[h - 1][w - 1] == 0:
    #         i += 1
    #         bom_map[h-1][w-1]=1
    #         BOMs.append([h, w])
    # print(H, W, M)
    # import pprint
    # pprint.pprint(BOMs)

    # H, W, M = 10,10,7
    # BOMs = [[2, 2], [2, 3], [1, 6], [4, 6], [7, 3], [10, 6], [5, 5]]
    solve(H, W, M, BOMs)
