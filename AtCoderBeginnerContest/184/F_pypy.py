# 解説を参考に作成
# import sys
# sys.setrecursionlimit(10 ** 6)
import bisect
# from collections import deque
# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, T, A):
    B = A[: N // 2]
    C = A[N // 2:]

    B_list = []
    for i in range(2 ** len(B)):
        tmp_sum = 0
        for j in range(len(B)):
            if i >> j & 1:
                tmp_sum += B[j]
        B_list.append(tmp_sum)
    B_list.sort()

    C_list = []
    for i in range(2 ** len(C)):
        tmp_sum = 0
        for j in range(len(C)):
            if i >> j & 1:
                tmp_sum += C[j]
        C_list.append(tmp_sum)
    C_list.sort()

    ans = 0
    for b in B_list:
        num = bisect.bisect_left(C_list, T - b)
        if num == len(C_list) or C_list[num] > T - b:
            num -= 1
        if b + C_list[num] <= T:
            ans = max(ans, b + C_list[num])
    print(ans)


if __name__ == '__main__':
    N, T = map(int, input().split())
    A = [int(i) for i in input().split()]
    solve(N, T, A)

    # # test
    # from random import randint
    # from func import random_str, random_ints
    #
    # N = 40
    # T = randint(10 ** 8, 10 ** 9)
    # A = [randint(10 ** 7, 10 ** 9) for _ in range(N)]
    # solve(N, T, A)
