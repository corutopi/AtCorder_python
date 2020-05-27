# x = iB + j とすると
# floor(A(iB + j) / B) - A * floor((iB + j/)B)
#   = A * i + floor(A * j / B) - A * i - A * floor(j / B)
#   = floor(A * j / B)
# なので, A * j が最大の時, floor(Ax/B) - A * floor(x/B) は最大となる.
# 0 <= j < B なので, x の値は
#   N < B の時, x = N, N >= B の時 x = B - 1
# となる.


from math import floor


def solve():
    A, B, N = map(int, input().split())
    x = min(N, B - 1)
    print(floor(A * x / B) - A * floor(x / B))


if __name__ == '__main__':
    solve()
