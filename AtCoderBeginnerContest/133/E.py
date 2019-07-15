import sys
sys.setrecursionlimit(10 ** 6)


def solve():
    N, K = map(int, input().split())
    AB = [[] for _ in range(N + 1)]
    for _ in range(N - 1):
        a, b = map(int, input().split())
        AB[a].append(b)
        AB[b].append(a)

    # AB = [sorted([int(i) for i in input().split()]) for _ in range(N - 1)]
    # AB.sort()
    print(dfs(AB, 1, 0, 0, 1, K, 0) % (10 ** 9 + 7))


def dfs(hen, cho, kai, ko, tag, K, oya):
    tag *= K - (ko - 1 if ko > 0 else 0) - (2 if kai >= 2 else kai)
    next_ko = hen[cho].copy()
    if oya != 0:
        next_ko.remove(oya)
    for i in range(len(next_ko)):
        tag = dfs(hen, next_ko[i], kai + 1, i + 1, tag, K, cho)
    return tag % (10 ** 9 + 7)


if __name__ == '__main__':
    solve()
