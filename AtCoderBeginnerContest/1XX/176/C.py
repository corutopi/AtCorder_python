# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, As):
    ans = 0
    for i in range(1, N):
        if As[i - 1] > As[i]:
            ans += As[i - 1] - As[i]
            As[i] = As[i - 1]
    print(ans)


if __name__ == '__main__':
    # S = input()
    N = int(input())
    # N, M = map(int, input().split())
    As = [int(i) for i in input().split()]
    # Bs = [int(i) for i in input().split()]
    solve(N, As)
