# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
inf = float('inf')
mod = 10 ** 9 + 7

from decorator import stop_watch


@stop_watch
def solve():
    S = 'aaa'
    for s in list(S):
        if S.count(s) != 2:
            print('No')
            return
    print('Yes')


if __name__ == '__main__':
    # S = input()
    # N = int(input())
    # N, M = map(int, input().split())
    # A = [int(i) for i in input().split()]
    # B = [int(i) for i in input().split()]
    # AB = [[int(i) for i in input().split()] for _ in range(N)]
    # P = [int(input()) for _ in range(N)]
    solve()

    # test
    from random import randint
    import tool.testcase as tt
    from tool.testcase import random_str, random_ints
    solve()
