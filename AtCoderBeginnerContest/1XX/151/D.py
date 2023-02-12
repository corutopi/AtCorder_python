# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
from collections import deque


# from decorator import stop_watch
#
#
# @stop_watch
def solve(H, W, Ss):
    Ss = ['#' + S + '#' for S in Ss]
    Ss = ['#' * (W + 2)] + Ss + ['#' * (W + 2)]
    # for S in Ss:
    #     print(S)
    ans = 0
    for i in range(1, H + 1):
        for j in range(1, W + 1):
            if Ss[i][j] == '#':
                continue
            visited = [[-1] * (W + 2) for _ in range(H + 2)]
            now = 0
            visited[i][j] = now
            q = deque([(i, j, now)])
            while q:
                x, y, n = q.popleft()
                # for v in visited:
                #     print(v)
                # input()
                for x1, y1 in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                    if Ss[x1][y1] == '.' \
                            and visited[x1][y1] < 0:
                        q.append((x1, y1, n + 1))
                        visited[x1][y1] = n + 1
            ans = max(ans, max([max(v) for v in visited]))

    print(ans)


if __name__ == '__main__':
    H, W = map(int, input().split())
    Ss = [input() for _ in range(H)]
    solve(H, W, Ss)
