def solve():
    N, M = map(int, input().split())
    L = []
    R = []
    for _ in range(M):
        tmp = input().split()
        L.append(int(tmp[0]))
        R.append(int(tmp[1]))
    ans = min(R) - max(L) + 1
    ans = ans if ans >= 0 else 0
    print(ans)


if __name__ == '__main__':
    solve()
