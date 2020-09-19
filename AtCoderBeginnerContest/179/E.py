# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, X, M):
    mods = [-1 for i in range(M)]
    number = 1
    mods[X] = number
    An = X ** 2 % M
    while mods[An] == -1:
        number += 1
        mods[An] = number
        # print('aaa', An, mods[An],An ** 2 % M)
        An = An ** 2 % M
    # print(An, mods[An], max(mods))
    loop_num = max(mods) - (mods[An] - 1)
    tag = (N - (mods[An] - 1)) % loop_num
    ans = 0
    for i in range(M):
        # if mods[i] - 1 == tag:
        #     print(i)
        #     return
        if mods[i] == -1:
            continue
        elif mods[i] < mods[An]:
            ans += i
        else:
            x = N - (mods[An] - 1)
            if tag != 0 and mods[i] - mods[An] < tag:
                ans += i * (x // loop_num + 1) if x >= 0 else 0
            else:
                ans += i * (x // loop_num) if x >= 0 else 0
    print(ans)



if __name__ == '__main__':
    # S = input()
    # N = int(input())
    N, X, M = map(int, input().split())
    # A = [int(i) for i in input().split()]
    # B = [int(i) for i in input().split()]
    # AB = [[int(i) for i in input().split()] for _ in range(N)]
    solve(N, X, M)

    # # test
    # from random import randint
    # from func import random_str
    # solve()
