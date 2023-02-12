# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from decorator import stop_watch
#
#
# @stop_watch
def solve(X, Y, A, B, C, Ps, Qs, Rs):
    inf = 10 ** 9 + 1
    Ps.sort(reverse=True)
    Qs.sort(reverse=True)
    Rs.sort(reverse=True)
    a = X - 1
    b = Y - 1
    c = 0
    while True:
        m = min(Ps[a] if a >= 0 else inf,
                Qs[b] if b >= 0 else inf,
                Rs[c])
        if m == Rs[c]:
            break
        elif m == Ps[a]:
            c += 1
            a -= 1
        elif m == Qs[b]:
            c += 1
            b -= 1
        if c == C:
            break

    ans = 0
    if a >= 0:
        ans += sum(Ps[:a + 1])
    if b >= 0:
        ans += sum(Qs[:b + 1])
    if c > 0:
        ans += sum(Rs[:c])

    print(ans)


if __name__ == '__main__':
    X, Y, A, B, C = map(int, input().split())
    Ps = [int(i) for i in input().split()]
    Qs = [int(i) for i in input().split()]
    Rs = [int(i) for i in input().split()]
    solve(X, Y, A, B, C, Ps, Qs, Rs)
