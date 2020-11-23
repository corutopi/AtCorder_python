# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# from decorator import stop_watch
#
#
# @stop_watch
def solve(n, a):
    ans1 = 0
    tmp_sum = 0
    tmp_code = 1
    for ai in a:
        tmp_sum += ai
        if tmp_sum == 0:
            ans1 += 1
            tmp_sum += - tmp_code
        now_code = tmp_sum // abs(tmp_sum)
        if tmp_code == now_code:
            x = (abs(tmp_sum) + 1) * (- now_code)
            ans1 += abs(x)
            tmp_sum += x
        tmp_code = - tmp_code
    ans2 = 0
    tmp_sum = 0
    tmp_code = -1
    for ai in a:
        tmp_sum += ai
        if tmp_sum == 0:
            ans2 += 1
            tmp_sum += - tmp_code
        now_code = tmp_sum // abs(tmp_sum)
        if tmp_code == now_code:
            x = (abs(tmp_sum) + 1) * (- now_code)
            ans2 += abs(x)
            tmp_sum += x
        tmp_code = - tmp_code
    print(min(ans1, ans2))


if __name__ == '__main__':
    n = int(input())
    a = [int(i) for i in input().split()]
    solve(n, a)

    # # test
    # from random import randint
    # from func import random_str, random_ints
    # for _ in range(10000):
    #     n = 10
    #     a = [randint(-10, 10) for _ in range(n)]
    #     solve(n, a)
