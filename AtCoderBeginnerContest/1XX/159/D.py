def cmb(n, r):
    import math
    if n < r:
        return 0
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))


# from deco import stop_watch
#
#
# @stop_watch
def solve(N, As):
    A_map = [0] * (N + 1)

    # make map
    for A in As:
        A_map[A] += 1

    # calc 'not remove' cmb
    g = 0
    for am in A_map:
        g += cmb(am, 2)

    # print result
    for A in As:
        if A > 0:
            print(g - (A_map[A] - 1))


if __name__ == '__main__':
    N = int(input())
    As = [int(i) for i in input().split()]
    solve(N, As)
