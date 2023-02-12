# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, Hs):
    Hs.reverse()
    ans = 'Yes'
    for i in range(N - 1):
        if Hs[i] < Hs[i + 1]:
            if abs(Hs[i] - Hs[i + 1]) == 1:
                Hs[i + 1] -= 1
            else:
                ans = 'No'
                break
    print(ans)


if __name__ == '__main__':
    # S = input()
    N = int(input())
    # N, M = map(int, input().split())
    Hs = [int(i) for i in input().split()]
    # Bs = [int(i) for i in input().split()]
    solve(N, Hs)
