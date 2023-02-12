# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, Vs):
    Vs.sort()
    ans = Vs[0]
    for i in range(1, N):
        ans = (ans + Vs[i]) / 2
    print(ans)


if __name__ == '__main__':
    # S = input()
    N = int(input())
    # N, M = map(int, input().split())
    Vs = [int(i) for i in input().split()]
    # Bs = [int(i) for i in input().split()]
    solve(N, Vs)
