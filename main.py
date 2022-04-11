N = int(input())
K = int(input())
while N < K:
  N += N
print(N - K)