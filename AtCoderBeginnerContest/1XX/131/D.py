# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, ABs):
    ABs.sort(key=lambda x: x[1])
    time = 0
    ans = 'Yes'
    for A, B in ABs:
        time += A
        if time > B:
            ans = 'No'
            break
    print(ans)


if __name__ == '__main__':
    # S = input()
    N = int(input())
    # N, M = map(int, input().split())
    ABs = [[int(i) for i in input().split()] for _ in range(N)]
    # Bs = [int(i) for i in input().split()]
    solve(N, ABs)
