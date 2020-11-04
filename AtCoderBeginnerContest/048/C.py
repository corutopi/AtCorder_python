# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, x, a):
    ans = sum(a)
    a_dsc = list(reversed(a))
    for a_tmp in [a, a_dsc]:
        ans_tmp = 0
        for i in range(1, N):
            if a_tmp[i - 1] + a_tmp[i] > x:
                diff = a_tmp[i - 1] + a_tmp[i] - x
                ans_tmp += diff
                if a_tmp[i] < diff:
                    a_tmp[i - 1] -= diff - a_tmp[i]
                    a_tmp[i] = 0
                else:
                    a_tmp[i] -= diff
        ans = min(ans, ans_tmp)
    print(ans)


if __name__ == '__main__':
    # S = input()
    # N = int(input())
    N, x = map(int, input().split())
    a = [int(i) for i in input().split()]
    solve(N, x, a)

    # # test
    # from random import randint
    # from func import random_str, random_ints
    # solve()
