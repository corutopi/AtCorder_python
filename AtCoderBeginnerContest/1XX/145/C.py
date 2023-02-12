# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, XY):
    from math import sqrt, factorial
    road_map = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            road_map[i][j] = sqrt((XY[i][0] - XY[j][0]) ** 2 +
                                  (XY[i][1] - XY[j][1]) ** 2)

    def dfs(now_town, visited, distance):
        visited[now_town] = 1
        if sum(visited) == N:
            return distance
        d = 0
        for i in range(N):
            if visited[i] == 0:
                d += dfs(i, visited.copy(), distance + road_map[now_town][i])
        return d

    sum_distance = 0
    for i in range(N):
        sum_distance += dfs(i, [0] * N, 0)

    print(sum_distance / factorial(N))


if __name__ == '__main__':
    # S = input()
    N = int(input())
    XY = []
    for _ in range(N):
        XY.append([int(i) for i in input().split()])
    solve(N, XY)
