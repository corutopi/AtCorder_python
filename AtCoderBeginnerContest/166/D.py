# 解説を参考に作成

def solve():
    X = int(input())
    A, B = 0, 0
    # A と B の差が最も小さい時(A - B = 1)に, ans < 10**9 となるのは
    # -118 <= A <= 119, -119 <= B <= 118 の場合となる.
    # A - B > 1 の場合でも同じ範囲だけ見れば十分となる.
    # A - B < 1 の場合は答えが負になるので, X >= 1 の制約から検討不要.
    for a in range(-118, 119 + 1):
        for b in range(-119, 118 + 1):
            if a ** 5 - b ** 5 == X:
                A, B = a, b
                break
    print(A, B)


if __name__ == '__main__':
    solve()
