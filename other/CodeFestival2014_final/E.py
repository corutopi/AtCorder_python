# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, R):
    dainari = [0] * N
    shonari = [0] * N
    dainari[0] = 1
    shonari[0] = 1
    for i in range(1, N):
        dai = 1
        sho = 1
        for j in reversed(range(i)):
            if R[i] > R[j]:
                dai = max(dai, shonari[j] + 1)
            elif R[i] < R[j]:
                sho = max(sho, dainari[j] + 1)
        dainari[i] = dai
        shonari[i] = sho
    ans = max(max(dainari), max(shonari))
    if ans < 3:
        ans = 0
    print(ans)


if __name__ == '__main__':
    N = int(input())
    R = [int(i) for i in input().split()]
    solve(N, R)

    # # test
    # from random import randint
    # from func import random_str, random_ints
    # N = 3000
    # R = [randint(-10 ** 5, 10 ** 5) for _ in range(N)]
    # solve(N, R)
