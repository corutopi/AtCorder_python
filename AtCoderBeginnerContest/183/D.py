# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, W, STP):
    P = []
    STN = []
    for i in range(N):
        s, t, p = STP[i]
        P.append(p)
        STN.append([s, 'S', i])
        STN.append([t, 'T', i])
    STN.sort(key=lambda x: x[0])
    ans = 'Yes'
    use = 0
    now = 0
    for m, x, n in STN:
        if m != now:
            if use > W:
                ans = 'No'
                break
            now = m
        if x == 'S':
            use += P[n]
        if x == 'T':
            use -= P[n]
    print(ans)


if __name__ == '__main__':
    N, W = map(int, input().split())
    STP = [[int(i) for i in input().split()] for _ in range(N)]
    solve(N, W, STP)

    # # test
    # from random import randint
    # from func import random_str, random_ints
    # solve()
