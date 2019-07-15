"""
B - Touitsu
"""


def solve():
    N = int(input())
    A = input()
    B = input()
    C = input()
    change_count = 0
    for i in range(N):
        if A[i] == B[i] == C[i]:
            pass
        elif (A[i] == B[i] or
              A[i] == C[i] or
              B[i] == C[i]):
            change_count += 1
        else:
            change_count += 2
    print(change_count)


if __name__ == '__main__':
    solve()
