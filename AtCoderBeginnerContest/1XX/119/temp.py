from operator import itemgetter

tik = [[1, 2], [7, 3], [4, 4], [5, 5], [3, 5], [2, 5], [9, 6], [8, 7], [6, 6]]
dic = {"1": 2, "7": 3, "4": 4, "5": 5, "3": 5, "2": 5, "9": 6, "8": 7, "6": 6}

n, k = map(int, input().split())
x = list(map(int, input().split()))
dp = [0] + [-1] * (n + 10)
q = []
for i in range(k):
    q.append([x[i], dic[str(x[i])]])

q = sorted(q, key=itemgetter(1), reverse=False)

s = []
p = 0
t = 0
for i in range(n):
    for j in range(k):
        if i + q[j][1] <= n:
            if dp[i] != -1:

                if dp[i] == 0:
                    ko = q[j][0]
                    dp[i + q[j][1]] = max(q[j][0], dp[i + q[j][1]])

                else:
                    ko = dp[i] + q[j][0]
                    dp[i + q[j][1]] = max(dp[i] * 10 + q[j][0], dp[i + q[j][1]])
    print(dp)
        # if i+q[j][1] ==n:
        # print(dp[20])
s = list(str(dp[n]))
s.sort()
s = s[::-1]
print(''.join(s))
