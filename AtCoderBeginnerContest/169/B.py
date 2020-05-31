def solve(N, As):
    ans = 1
    _As = sorted(As)
    border = 10 ** 18
    for a in _As:
        ans *= a
        if ans > border:
            print(-1)
            return
    print(ans)


if __name__ == '__main__':
    N = int(input())
    As = [int(i) for i in input().split()]
    solve(N, As)
