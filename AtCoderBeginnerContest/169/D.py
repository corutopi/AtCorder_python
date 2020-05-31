def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n ** 0.5 // 1)) + 1):
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
            arr.append([i, cnt])
    if temp != 1:
        arr.append([temp, 1])
    if arr == []:
        arr.append([n, 1])

    return arr


def solve(N):
    fact = factorization(N)
    ans = 0

    if N == 1:
        print(0)
        return

    for f in fact:
        s, c = f
        i = 1
        while True:
            if c >= i:
                c -= i
                ans += 1
            else:
                break
            i += 1
    print(ans)


if __name__ == '__main__':
    N = int(input())
    solve(N)
