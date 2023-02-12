

def solve(N, K, Hs):
    Hs.sort(reverse=True)
    ans = 0
    for h in Hs:
        if K > 0:
            K -= 1
        else:
            ans += h
    print(ans)


if __name__ == '__main__':
    N, K = map(int, input().split())
    Hs = [int(i) for i in input().split()]
    solve(N, K, Hs)
