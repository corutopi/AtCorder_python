def solve():
    H, W = map(int, input().split())
    mass = [[0] * W for _ in range(H)]
    for Hi in range(H):
        massHi = [0 if s == '.' else 1 for s in list(input())]
        for Wi in range(W):
            mass[Hi][Wi] = massHi[Wi]

    # import pprint
    # pprint.pprint(mass)

    result = 0
    for Hi in range(H):
        for Wi in range(W):
            if mass[Hi][Wi] == 1:
                break
            sub_result = 100000000
            for Hi2 in range(H):
                for Wi2 in range(W):
                    if mass[Hi2][Wi2] == 1:
                        abs_score = abs(Hi2 - Hi) + abs(Wi2 - Wi)
                        sub_result = min(sub_result,
                                         abs_score)
            result = max(result, sub_result)
    print(result)


if __name__ == '__main__':
    solve()
