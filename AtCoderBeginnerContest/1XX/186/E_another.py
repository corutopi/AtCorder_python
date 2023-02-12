"""
以下を参考に作成
https://twitter.com/kyopro_friends/status/1341216644727676928

s + k * x ≡ 0 mod n を解く(xを求める).
鳥の巣原理から x <= n のため,
    x = im + j (0 <= i, j <= m = n**0.5)
と表せる.
j が 0 ～ m の時の位置(s + k * j mod n)を前計算し,mapに持っておく(jmap).
    s + k * (im + j) ≡ 0 mod n
    s + k * j + k * im ≡ 0 mod n
    ((s + k * j) mod n) + (k * im mod n) = n or 0 ≡ 0 mod n
と表せるため, ある i に対して
    (k * im mod n) + p = n or 0
となるような p が jmap に存在していれば, その時の im + j が答えとなる.
これを i が 0 ～ m の範囲で全探索し, 存在していなければ -1 となる.
@Baby-Step Giant-Step
"""
# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
from collections import Counter

inf = float('inf')
mod = 10 ** 9 + 7

# from decorator import stop_watch
#
#
# @stop_watch
def solve(T, NSK):
    for n, s, k in NSK:
        m = int(n ** 0.5) + 1
        jmap = {}
        for j in range(m):
            tmp = (s + k * j) % n
            jmap.setdefault(tmp, j)
            jmap[tmp] = min(j, jmap[tmp])
        for i in range(m):
            tmp = (n - (k * i * m) % n) % n
            if jmap.get(tmp, - 1) >= 0:
                print(i * m + jmap[tmp])
                break
        else:
            print(-1)


if __name__ == '__main__':
    T = int(input())
    NSK = [[int(i) for i in input().split()] for _ in range(T)]
    solve(T, NSK)

    # # test
    # from random import randint
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # T = 100
    # NSK = []
    # for _ in range(T):
    #     N = randint(1, 10 ** 9)
    #     S = randint(1, N - 1)
    #     K = randint(1, 10 ** 9)
    #     NSK.append([N, S, K])
    # solve(T, NSK)
