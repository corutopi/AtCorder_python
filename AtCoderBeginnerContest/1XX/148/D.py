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
    i = 1
    for A in As:
        if A == i:
            i += 1
        else:
            ans += 1
    ans = -1 if ans == N else ans
    print(ans)


if __name__ == '__main__':
    # S = input()
    N = int(input())
    # N, M = map(int, input().split())
    As = [int(i) for i in input().split()]
    # Bs = [int(i) for i in input().split()]
    solve(N, As)
