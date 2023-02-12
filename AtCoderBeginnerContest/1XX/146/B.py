

def solve():
    N = int(input())
    S = input()
    alp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alp = list(alp)
    ans = ''
    for s in S:
        i = (alp.index(s) + N) % 26
        ans += alp[i]
    print(ans)


if __name__ == '__main__':
    solve()
