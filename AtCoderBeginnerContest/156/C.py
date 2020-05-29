

def solve(N ,Xs):
    ans = float('inf')
    for i in range(100):
        _sum = sum([(x - i) ** 2 for x in Xs])
        ans = min(ans, _sum)

    print(ans)


if __name__ == '__main__':
    N = int(input())
    Xs = [int(i) for i in input().split()]
    solve(N, Xs)
