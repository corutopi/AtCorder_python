# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# import string
from math import ceil, floor

inf = float('inf')
mod = 10 ** 9 + 7
mod2 = 998244353

# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, M, AB, K, CD):
    ans = 0
    for i in range(2 ** K):
        tmp = [0] * (N + 1)
        for j in range(K):
            if i >> j & 1:
                tmp[CD[j][0]] += 1
            else:
                tmp[CD[j][1]] += 1
        ans_tmp = 0
        for a, b in AB:
            if tmp[a] > 0 and tmp[b] > 0:
                ans_tmp += 1
        ans = max(ans_tmp, ans)
    print(ans)


if __name__ == '__main__':
    N, M = map(int, input().split())
    AB = [[int(i) for i in input().split()] for _ in range(M)]
    K = int(input())
    CD = [[int(i) for i in input().split()] for _ in range(K)]
    solve(N, M, AB, K, CD)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
