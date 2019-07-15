def solve():
    N, K = map(int, input().split())
    S = input()
    list_S = list(S)
    list_S[K - 1] = list_S[K - 1].lower()
    print(''.join(list_S))


if __name__ == '__main__':
    solve()
