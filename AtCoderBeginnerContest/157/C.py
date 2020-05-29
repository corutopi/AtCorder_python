def solve(N, M, sc):
    ans = 0
    digits = [-1] * N
    for s, c in sc:
        _digits = N - s
        if digits[_digits] == -1:
            digits[_digits] = c
        elif digits[_digits] != c:
            ans = -1
            break

    if digits[-1] == 0 and N > 1:
        ans = -1

    if digits[-1] == -1:
        digits[-1] = 1 if N > 1 else 0

    for d in range(N):
        digits[d] = 0 if digits[d] == -1 else digits[d]

    if ans != -1:
        ans = sum([digits[i] * (10 ** i) for i in range(N)])

    print(ans)


if __name__ == '__main__':
    N, M = map(int, input().split())
    sc = []
    for _ in range(M):
        sc.append(tuple(map(int, input().split())))
    solve(N, M, sc)
