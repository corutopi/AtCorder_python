# from decorator import stop_watch
#
#
# @stop_watch
def solve(S, Q, Qs):
    rev_flg = False
    bef = ''
    aft = ''
    for q in Qs:
        if q[0] == 1:
            rev_flg = not rev_flg
            bef, aft = aft, bef
        else:
            bf = q[1]
            if bf == 1:
                bef += q[2]
            elif bf == 2:
                aft += q[2]
    bef = bef[::-1]
    if rev_flg:
        S = S[::-1]
    print(bef + S + aft)


if __name__ == '__main__':
    # # handmade
    # S = 'h' * 10 ** 5
    # Q = 2 * 10 ** 5
    # Qs = []
    # for i in range(Q - 1):
    #     if i % 2 == 0:
    #         Qs.append([2, 1, 'a'])
    #     else:
    #         Qs.append([2, 2, 'b'])
    # Qs.append([1])

    # input
    S = input()
    Q = int(input())
    Qs = []
    i = 0
    for _ in range(Q):
        s = input()
        i += 1
        if s[0] == '1':
            q = [1]
        else:
            q = s.split()
            q[0] = int(q[0])
            q[1] = int(q[1])
        Qs.append(q)

    solve(S, Q, Qs)
