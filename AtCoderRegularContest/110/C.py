# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, P):
    P = [0] + P
    toLeft = 0
    toRight = 0
    for i in range(1, N + 1):
        if i == P[i]:
            print(-1)
            return
        if P[i] - i > 0:
            toRight += abs(P[i] - i)
        else:
            toLeft += abs(P[i] - i)
    if not (toLeft == toRight == N - 1):
        print(-1)
        return
    cnt = 1
    ans = []
    while cnt != 0:
        cnt = 0
        for i in range(1, N):
            if P[i + 1] - (i + 1) < 0 < abs(P[i] - i):
                P[i], P[i + 1] = P[i + 1], P[i]
                ans.append(i)
                cnt += 1
        for i in range(N, 1, -1):
            if P[i] - i < 0 < P[i - 1] - (i - 1):
                P[i], P[i - 1] = P[i - 1], P[i]
                ans.append(i - 1)
                cnt += 1
    # print(P[1:])
    [print(a) for a in ans]


if __name__ == '__main__':
    N = int(input())
    P = [int(i) for i in input().split()]
    solve(N, P)

    # # test
    # from random import randint
    # from func import random_str, random_ints
    # solve()
