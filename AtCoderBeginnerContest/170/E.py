"""
解説と以下を参考に作成
    https://atcoder.jp/contests/abc170/submissions/18391473
"""
# import sys
# sys.setrecursionlimit(10 ** 6)
import bisect

# from collections import deque

mod = 10 ** 9 + 7

import heapq
import collections


class SuperHeapq:
    """
    削除する際の値を記録しておくことでheapqをより高速に処理する.
    依存関係:
        import heapq
        import collections

    ↓からほぼ丸々もらった.
    https://atcoder.jp/contests/abc170/submissions/18391473
    """

    def __init__(self):
        self.q = []
        self.rmv = collections.Counter()
        self.cnt = 0

    def q(self):
        return self.q

    def length(self):
        return self.cnt

    def refresh(self):
        while len(self.q) > 0:
            key = self.q[0]
            if self.rmv[key] > 0:
                self.rmv[key] -= 1
                heapq.heappop(self.q)
            else:
                break

    def minVal(self):
        if self.length() == 0:
            return None
        return self.q[0]

    def pop(self):
        if self.length() == 0:
            return None
        self.cnt -= 1
        self.refresh()
        return heapq.heappop(self.q)

    def push(self, x):
        if x is None:
            return
        self.cnt += 1
        heapq.heappush(self.q, x)

    def remove(self, x):
        if x is None:
            return
        self.cnt -= 1
        self.rmv[x] += 1
        self.refresh()


# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, Q, AB, CD):
    AB = [[0, 0]] + AB
    child_code = [AB[i][0] * 10 ** 6 + i for i in range(N + 1)]
    en = [SuperHeapq() for _ in range(2 * 10 ** 5 + 1)]
    for i in range(1, N + 1):
        a, b = AB[i]
        en[b].push(-child_code[i])  # 園では負の値で管理(最大値を取り出すため)

    maximer = SuperHeapq()
    for e in en:
        if e.length() == 0:
            continue
        maximer.push(-e.minVal())  # 最強園児は正の値で管理(最小値を取り出すため)

    for c, d in CD:
        cc = child_code[c]
        from_en = en[AB[c][1]]
        to_en = en[d]

        # 転園元の処理
        maximer.remove(-from_en.minVal())
        from_en.remove(-cc)
        if from_en.length() != 0:
            maximer.push(-from_en.minVal())

        # 転園先の処理
        if to_en.length() != 0:
            maximer.remove(-to_en.minVal())
        to_en.push(-cc)
        maximer.push(-to_en.minVal())

        print(maximer.minVal() // 10 ** 6)
        AB[c][1] = d


if __name__ == '__main__':
    N, Q = map(int, input().split())
    AB = [[int(i) for i in input().split()] for _ in range(N)]
    CD = [[int(i) for i in input().split()] for _ in range(Q)]
    solve(N, Q, AB, CD)

    # # test
    # from random import randint
    # from func import random_str, random_ints
    # N, Q = 2 * 10 ** 5, 2 * 10 ** 5
    # AB = [[randint(1, 10 ** 9), randint(1, 2 * 10 ** 5)] for _ in range(N)]
    # CD = [[randint(1, N), randint(1, 2 * 10 ** 5)] for _ in range(Q)]
    # solve(N, Q, AB, CD)
