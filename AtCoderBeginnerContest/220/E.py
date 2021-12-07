# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# import string
from math import ceil, floor

inf = float('inf')
# mod = 10 ** 9 + 7
mod = 998244353

# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, D):
    # 2 ** x の前計算
    e2 = [1]
    for _ in range(max(N, D)):
        e2.append(e2[-1] * 2 % mod)
    # 2 ** inf のTreeで、頂点を含む距離Dとなるパスの個数計算
    ps = []
    for i in range(D + 1):
        x, y = i, D - i
        ps.append((e2[max(x - 1, 0)] * e2[max(y - 1, 0)] * 2) % mod)
    cs_ps = [0]
    for p in ps:
        cs_ps.append((cs_ps[-1] + p) % mod)
    # 各頂点Aiで、AiとAi以上の数字のみを含む距離Dとなるパスの個数計算
    ans = 0
    for n in range(N):
        if N - n - 1 >= D:
            ans += cs_ps[-1] * e2[n]
        elif (N - n - 1) * 2 >= D:
            ans += (cs_ps[N - n] - cs_ps[D - (N - n) + 1]) * e2[n]
        else:
            break
        ans %= mod

    print(ans)


if __name__ == '__main__':
    N, D = map(int, input().split())
    solve(N, D)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve(3, 1)
    # N = 5
    # for d in range(1, 20):
    #     solve(N, d)
