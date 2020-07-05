# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, As):
    import math
    As = sorted(As, reverse=True)
    ans = As[0]
    for i in range(2, N):
        ans += As[math.ceil((i + 1) / 2) - 1]
    print(ans)



if __name__ == '__main__':
    # S = input()
    N = int(input())
    # N, M = map(int, input().split())
    As = [int(i) for i in input().split()]
    # Bs = [int(i) for i in input().split()]
    solve(N, As)
