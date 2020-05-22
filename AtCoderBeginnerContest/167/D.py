def solve():
    N, K = map(int, input().split())
    As = [int(i) - 1 for i in input().split()]

    visited = [-1 for _ in range(N)]
    roop_As = [0]
    now_i = 0
    visited[now_i] = 0
    for _ in range(K):
        now_i = As[now_i]
        if visited[now_i] >= 0:
            break
        roop_As.append(now_i)
        visited[now_i] = len(roop_As) - 1

    if K < len(roop_As):
        print(roop_As[-1] + 1)
    else:
        roop_As = roop_As[visited[now_i]:]
        print(roop_As[(K - visited[now_i]) % len(roop_As)] + 1)


if __name__ == '__main__':
    solve()
