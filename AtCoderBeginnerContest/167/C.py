def solve():
    N, M, X = map(int, input().split())
    C = []
    A = []
    for _ in range(N):
        tmp = [int(i) for i in input().split()]
        C.append(tmp[0])
        A.append(tmp[1:])

    result = 10 ** 5 * 12 + 1
    for i in range(2 ** N):
        b = ('0' * N + format(i, 'b'))[-N:]
        r = [0] * M
        sub_res = 0
        for j, s in enumerate(b):
            if int(s) == 1:
                sub_res += C[j]
                for k in range(M):
                    r[k] += A[j][k]
        if all([rx >= X for rx in r]):
            result = min(result, sub_res)
    if result != 10 ** 5 * 12 + 1:
        print(result)
    else:
        print(-1)


if __name__ == '__main__':
    solve()
