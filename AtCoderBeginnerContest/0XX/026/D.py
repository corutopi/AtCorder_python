# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# from decorator import stop_watch
#
#
# @stop_watch
def solve(A, B, C):
    import math
    cycle = 2 / C
    t = 0
    start = 0
    end = 0
    while True:
        tmp = A * t + B * math.sin(C * t * math.pi)
        if tmp >= 100:
            end = t
            break
        else:
            start = t
        t += cycle

    ans = 0
    for _ in range(100):
        s = start
        e = end
        tt = s
        for i in range(100):
            tt += (e - s) / 100
            tmp = A * tt + B * math.sin(C * tt * math.pi)
            if tmp >= 100:
                end = tt
                break
            else:
                start = tt
        ans = tt
    print(ans)
    # print(A * ans + B * math.sin(C * ans * math.pi))


if __name__ == '__main__':
    A, B, C = map(int, input().split())
    solve(A, B, C)
    # import math
    # t = 1.63372043395339
    # print(A * t)
    # print(B * math.sin(C * t * math.pi))
    # print(A * t + B * math.sin(C * t * math.pi))

    # # test
    # from random import randint
    # from func import random_str, random_ints
    # solve()
