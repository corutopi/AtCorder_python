# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# from decorator import stop_watch
#
#
# @stop_watch
def solve(H, W, K, Cxx):
    ans = 0
    for i in range(2 ** H):
        for j in range(2 ** W):
            cnt = 0
            for h in range(H):
                if i >> h & 1 == 1:
                    continue
                for w in range(W):
                    if j >> w & 1 == 1:
                        continue
                    if Cxx[h][w] == '#':
                        cnt += 1
            if cnt == K:
                ans += 1
    print(ans)



if __name__ == '__main__':
    # S = input()
    # N = int(input())
    H, W, K = map(int, input().split())
    Cxx = [input() for _ in range(H)]
    # As = [int(i) for i in input().split()]
    # Bs = [int(i) for i in input().split()]
    solve(H, W, K, Cxx)
