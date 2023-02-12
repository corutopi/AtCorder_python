# 解説を参考に作成

# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
from collections import deque
# from decorator import stop_watch
#
#
# @stop_watch
def solve(H, W, C, D, Ss):
    cost_map = [[-1] * (W + 4) for _ in range(H + 4)]
    Ss = ['#' * (W + 4)] * 2 + ['##' + S + '##' for S in Ss] + ['#' * (W + 4)] * 2
    C = [c + 1 for c in C]
    D = [d + 1 for d in D]
    cost = 0
    ans = -1
    dq = deque()
    dq.append(C)
    while dq:
        next_dq = deque()
        flg = False
        while dq:
            h, w = dq.popleft()
            if h == D[0] and w == D[1]:
                ans = cost
                flg = True
                break
            if cost_map[h][w] >= 0:
                continue
            cost_map[h][w] = cost
            for i in range(h - 2, h + 2 + 1):
                for j in range(w - 2, w + 2 + 1):
                    if Ss[i][j] == '#':
                        continue
                    if cost_map[i][j] >= 0:
                        continue
                    if abs(h - i) + abs(w - j) == 1:
                        dq.append([i, j])
                    else:
                        next_dq.append([i, j])
        if flg:
            break
        dq = next_dq
        cost += 1
    print(ans)


if __name__ == '__main__':
    # S = input()
    # N = int(input())
    H, W = map(int, input().split())
    C = [int(i) for i in input().split()]
    D = [int(i) for i in input().split()]
    Ss = [input() for _ in range(H)]
    # Bs = [int(i) for i in input().split()]
    solve(H, W, C, D, Ss)
