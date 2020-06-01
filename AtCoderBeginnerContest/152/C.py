

def solve(N, Ps):
    ans = 0
    target = Ps[0]
    for p in Ps:
        if p <= target:
            ans += 1
            target = p
    print(ans)


if __name__ == '__main__':
    N = int(input())
    Ps = [int(i) for i in input().split()]
    solve(N, Ps)
