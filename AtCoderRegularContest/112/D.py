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
def solve(H, W, S):
    S = ['X' * (W + 2)] + ['X' + s + 'X' for s in S] + ['X' * (W + 2)]
    is_reach_H = [[0] * (W + 2) for _ in range(H + 2)]
    is_reach_W = [[0] * (W + 2) for _ in range(H + 2)]
    sum_H = [0] * (H + 2)
    sum_H[1] = W
    sum_H[H] = W
    sum_W = [0] * (W + 2)
    sum_W[1] = H
    sum_W[W] = H
    dq = deque([(1, 1), (1, W), (H, 1), (H, W)])
    while dq:
        h, w = dq.popleft()
        is_reach_H[h][w] = 1
        is_reach_W[h][w] = 1
        for u in range(1, H + 1):
            new_h = h - u
            new_w = w
            if S[new_h][new_w] == 'X': break
            if S[new_h][new_w] == '#' :
                if is_reach_H[new_h][new_w] == 0:
                    is_reach_H[new_h][new_w] = 1
                    is_reach_W[new_h][new_w] = 1
                    sum_H[new_h] += 1
                    sum_W[new_w] += 1
                    dq.append((new_h, new_w))
                break
            if S[new_h][new_w] == '.' and is_reach_H[new_h][new_w] == 0:
                is_reach_H[new_h][new_w] = 1
                is_reach_W[new_h][new_w] = 1
                sum_H[new_h] += 1
                sum_W[new_w] += 1
        for d in range(1, H + 1):
            new_h = h + d
            new_w = w
            if S[new_h][new_w] == 'X': break
            if S[new_h][new_w] == '#' :
                if is_reach_H[new_h][new_w] == 0:
                    is_reach_H[new_h][new_w] = 1
                    is_reach_W[new_h][new_w] = 1
                    sum_H[new_h] += 1
                    sum_W[new_w] += 1
                    dq.append((new_h, new_w))
                break
            if S[new_h][new_w] == '.' and is_reach_H[new_h][new_w] == 0:
                is_reach_H[new_h][new_w] = 1
                is_reach_W[new_h][new_w] = 1
                sum_H[new_h] += 1
                sum_W[new_w] += 1
        for l in range(1, W + 1):
            new_h = h
            new_w = w - l
            if S[new_h][new_w] == 'X': break
            if S[new_h][new_w] == '#' :
                if is_reach_H[new_h][new_w] == 0:
                    is_reach_H[new_h][new_w] = 1
                    is_reach_W[new_h][new_w] = 1
                    sum_H[new_h] += 1
                    sum_W[new_w] += 1
                    dq.append((new_h, new_w))
                break
            if S[new_h][new_w] == '.' and is_reach_H[new_h][new_w] == 0:
                is_reach_H[new_h][new_w] = 1
                is_reach_W[new_h][new_w] = 1
                sum_H[new_h] += 1
                sum_W[new_w] += 1
        for r in range(1, W + 1):
            new_h = h
            new_w = w + r
            if S[new_h][new_w] == 'X': break
            if S[new_h][new_w] == '#' :
                if is_reach_H[new_h][new_w] == 0:
                    is_reach_H[new_h][new_w] = 1
                    is_reach_W[new_h][new_w] = 1
                    sum_H[new_h] += 1
                    sum_W[new_w] += 1
                    dq.append((new_h, new_w))
                break
            if S[new_h][new_w] == '.' and is_reach_H[new_h][new_w] == 0:
                is_reach_H[new_h][new_w] = 1
                is_reach_W[new_h][new_w] = 1
                sum_H[new_h] += 1
                sum_W[new_w] += 1
    # [print(''.join([str(iirr) for iirr in ir])) for ir in is_reach_H]

    ans_H = 0
    for hh in range(1, H + 1):
        if sum_H[hh] >= W: continue
        ans_H += 1
        dq = deque([(hh, 1)])
        while dq:
            h, w = dq.popleft()
            is_reach_H[h][w] = 1
            for u in range(1, H + 1):
                new_h = h - u
                new_w = w
                if S[new_h][new_w] == 'X': break
                if S[new_h][new_w] == '#':
                    if is_reach_H[new_h][new_w] == 0:
                        is_reach_H[new_h][new_w] = 1
                        sum_H[new_h] += 1
                        dq.append((new_h, new_w))
                    break
                if S[new_h][new_w] == '.' and is_reach_H[new_h][new_w] == 0:
                    is_reach_H[new_h][new_w] = 1
                    sum_H[new_h] += 1
            for d in range(1, H + 1):
                new_h = h + d
                new_w = w
                if S[new_h][new_w] == 'X': break
                if S[new_h][new_w] == '#':
                    if is_reach_H[new_h][new_w] == 0:
                        is_reach_H[new_h][new_w] = 1
                        sum_H[new_h] += 1
                        dq.append((new_h, new_w))
                    break
                if S[new_h][new_w] == '.' and is_reach_H[new_h][new_w] == 0:
                    is_reach_H[new_h][new_w] = 1
                    sum_H[new_h] += 1
            for l in range(1, W + 1):
                new_h = h
                new_w = w - l
                if S[new_h][new_w] == 'X': break
                if S[new_h][new_w] == '#':
                    if is_reach_H[new_h][new_w] == 0:
                        is_reach_H[new_h][new_w] = 1
                        sum_H[new_h] += 1
                        dq.append((new_h, new_w))
                    break
                if S[new_h][new_w] == '.' and is_reach_H[new_h][new_w] == 0:
                    is_reach_H[new_h][new_w] = 1
                    sum_H[new_h] += 1
            for r in range(1, W + 1):
                new_h = h
                new_w = w + r
                if S[new_h][new_w] == 'X': break
                if S[new_h][new_w] == '#':
                    if is_reach_H[new_h][new_w] == 0:
                        is_reach_H[new_h][new_w] = 1
                        sum_H[new_h] += 1
                        dq.append((new_h, new_w))
                    break
                if S[new_h][new_w] == '.' and is_reach_H[new_h][new_w] == 0:
                    is_reach_H[new_h][new_w] = 1
                    sum_H[new_h] += 1

    ans_W = 0
    for ww in range(1, W + 1):
        # if sum([ir[ww] for ir in is_reach_W]) == H: continue
        if sum_W[ww] >= H: continue
        ans_W += 1
        dq = deque([(1, ww)])
        while dq:
            h, w = dq.popleft()
            is_reach_W[h][w] = 1
            for u in range(1, H + 1):
                new_h = h - u
                new_w = w
                if S[new_h][new_w] == 'X': break
                if S[new_h][new_w] == '#':
                    if is_reach_W[new_h][new_w] == 0:
                        is_reach_W[new_h][new_w] = 1
                        sum_W[new_w] += 1
                        dq.append((new_h, new_w))
                    break
                if S[new_h][new_w] == '.' and is_reach_W[new_h][new_w] == 0:
                    is_reach_W[new_h][new_w] = 1
                    sum_W[new_w] += 1
            for d in range(1, H + 1):
                new_h = h + d
                new_w = w
                if S[new_h][new_w] == 'X': break
                if S[new_h][new_w] == '#':
                    if is_reach_W[new_h][new_w] == 0:
                        is_reach_W[new_h][new_w] = 1
                        sum_W[new_w] += 1
                        dq.append((new_h, new_w))
                    break
                if S[new_h][new_w] == '.' and is_reach_W[new_h][new_w] == 0:
                    is_reach_W[new_h][new_w] = 1
                    sum_W[new_w] += 1
            for l in range(1, W + 1):
                new_h = h
                new_w = w - l
                if S[new_h][new_w] == 'X': break
                if S[new_h][new_w] == '#':
                    if is_reach_W[new_h][new_w] == 0:
                        is_reach_W[new_h][new_w] = 1
                        sum_W[new_w] += 1
                        dq.append((new_h, new_w))
                    break
                if S[new_h][new_w] == '.' and is_reach_W[new_h][new_w] == 0:
                    is_reach_W[new_h][new_w] = 1
                    sum_W[new_w] += 1
            for r in range(1, W + 1):
                new_h = h
                new_w = w + r
                if S[new_h][new_w] == 'X': break
                if S[new_h][new_w] == '#':
                    if is_reach_W[new_h][new_w] == 0:
                        is_reach_W[new_h][new_w] = 1
                        sum_W[new_w] += 1
                        dq.append((new_h, new_w))
                    break
                if S[new_h][new_w] == '.' and is_reach_W[new_h][new_w] == 0:
                    is_reach_W[new_h][new_w] = 1
                    sum_W[new_w] += 1
    print(min(ans_H, ans_W))


if __name__ == '__main__':
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    solve(H, W, S)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    #
    # H, W = 1000, 1000
    # S = [random_str(W, '...................................#') for _ in range(H)]
    # solve(H, W, S)
