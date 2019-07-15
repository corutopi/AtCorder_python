

def solve():
    S = input()
    for s in list(S):
        if S.count(s) != 2:
            print('No')
            return
    print('Yes')


if __name__ == '__main__':
    solve()
