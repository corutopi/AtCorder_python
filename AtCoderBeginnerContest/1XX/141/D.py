# import sys
# sys.setrecursionlimit(10 ** 6)
import bisect
# from collections import deque
# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, M, As):
    prices = sorted(As, reverse=True) + [0]
    halfed_idx = []
    n = 0
    idx = 0
    for _ in range(M):
        if len(halfed_idx) == 0:
            prices[n] //= 2
            halfed_idx.append(n)
            n += 1
        else:
            if prices[n] > prices[halfed_idx[idx]]:
                prices[n] //= 2
                halfed_idx.append(n)
                n += 1
            else:
                prices[halfed_idx[idx]] //= 2
                halfed_idx.append(halfed_idx[idx])
                idx += 1
    print(sum(prices))


def solve2(N, M, As):
    """later (ave 2.3 second)"""
    As.sort()
    for i in range(M):
        p = As.pop() // 2
        As.insert(bisect.bisect_right(As, p), p)
    print(sum(As))


if __name__ == '__main__':
    N, M = map(int, input().split())
    As = [int(i) for i in input().split()]

    # N, M = 10 ** 5, 10 ** 5
    # from random import randint
    # As = [randint(1, 10 ** 9) for _ in range(N)]
    solve(N, M, As)
    # solve2(N, M, As)
