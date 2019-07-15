def solve():
    H, W, N = map(int, input().split())
    sr, sc = map(int, input().split())
    S = list(input())
    T = list(input())

    # to left
    vec = 'L'
    anv = 'R'
    border = 1
    winner = 'YES'
    result = sc
    addition = -1
    out_mass_func = lambda x: x < border
    for i in range(len(S)):
        if S[i] == vec:
            result += addition
        if out_mass_func(result):
            winner = 'NO'
            break
        if T[i] == anv and result < border:
            result -= addition
    # print('left', result)
    # to right
    if winner == 'YES':
        vec = 'R'
        anv = 'L'
        border = W
        winner = 'YES'
        result = sc
        addition = 1
        out_mass_func = lambda x: x > border
        for i in range(len(S)):
            if S[i] == vec:
                result += addition
            if out_mass_func(result):
                winner = 'NO'
                break
            if T[i] == anv and (1 < result):
                result -= addition
        # print('right', result)
    # to top
    if winner == 'YES':
        vec = 'U'
        anv = 'D'
        border = 1
        winner = 'YES'
        result = sr
        addition = -1
        out_mass_func = lambda x: x < border
        for i in range(len(S)):
            if S[i] == vec:
                result += addition
            if out_mass_func(result):
                winner = 'NO'
                break

            if T[i] == anv and (result < border):
                result -= addition
        # print('top', result)
    # to bottom
    if winner == 'YES':
        vec = 'D'
        anv = 'U'
        border = H
        winner = 'YES'
        result = sr
        addition = 1
        out_mass_func = lambda x: x > border
        for i in range(len(S)):
            if S[i] == vec:
                result += addition
            if out_mass_func(result):
                winner = 'NO'
                break
            if T[i] == anv and 1 < result:
                result -= addition
        # print('bottom', result)
    print(winner)


if __name__ == '__main__':
    solve()
