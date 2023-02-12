"""
解説を参考に作成
- 解説記載の内容から, 修行前の最適解は A を昇順, F を降順に並べ, 各 i に対して A[i] と F[i] をペアにすればよい.
- ここで, 各 A に対して完食時間が x 以下になるような最小回数の修行させるとする.
- 修行後の A を A' とすると,
    A'[i] * F[i] < x
    A'[i] < x / F[i]
    A'[i] = floor(x / F[i])
- さらにここで,
    F[i] >= F[i + 1]  (Fは降順に並んでいる)より,
    floor(x / F[i]) <= floor(x / F[i + 1])
    A'[i] <= A'[i + 1]
- よって, 最適な修行をした後でも修行前と同じく最適解の条件を満たしている.
- そのため, 各 A の完食時間を x 以下とすることが可能かどうかを調べるには修行前の最適解それぞれに対して単純な演算を行えばよい(O(N))
- あとは x を2分探索すればよい. 制約における x の最大値は (10 ** 6) ** 2) = 10 ** 12 なので, O(N * log2x) で十分間に合う.
- 2 * 10 ** 5 * log(10 ** 12) ≒ 8 * 10 ** 6 だがpythonだと間に合わなかったでござる.
"""
# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
from math import ceil, floor

inf = float('inf')
mod = 10 ** 9 + 7
mod2 = 998244353


def binary_search(ok, ng, solve):
    """2分探索"""
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if solve(mid):
            ok = mid
        else:
            ng = mid
    return ok


# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, K, A, F):
    A.sort()
    F.sort(reverse=True)

    def func(x):
        training = 0
        for i in range(N):
            training += max(0, A[i] - floor(x / F[i]))
        if training <= K:
            return True
        else:
            return False

    print(binary_search(10 ** 12, -1, func))


if __name__ == '__main__':
    N, K = map(int, input().split())
    A = [int(i) for i in input().split()]
    F = [int(i) for i in input().split()]
    solve(N, K, A, F)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # N, K = 2 * 10 ** 5, randint(1, 10 ** 9)
    # A = [randint(1, 10 ** 6) for _ in range(N)]
    # F = [randint(1, 10 ** 6) for _ in range(N)]
    # solve(N, K, A, F)
