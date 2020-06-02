from heapq import heappush, heappop


def solve(N, X, Y):
    ans = [0] * (N)

    G = [[] for _ in range(N + 1)]
    for i in range(1, N):
        G[i].append(i + 1)
        G[i + 1].append(i)
    G[X].append(Y)
    G[Y].append(X)

    def dfs(vertex):
        nears = [float('inf')] * (N + 1)
        depth = 0
        que = [[depth, vertex]]
        while que:
            d, v = heappop(que)
            if d < nears[v]:
                nears[v] = d
                for g in G[v]:
                    heappush(que, [d + 1, g])
            # print(que)
        return nears

    for i in range(1, N):
        # dfs
        nears = dfs(i)
        # print(nears)
        for j in range(i + 1, N + 1):
            ans[nears[j]] += 1

    for i in ans[1:]:
        print(i)


if __name__ == '__main__':
    N, X, Y = map(int, input().split())
    solve(N, X, Y)
