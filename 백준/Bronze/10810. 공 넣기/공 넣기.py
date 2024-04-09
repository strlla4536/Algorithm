import sys
input = sys.stdin.readline

N, M = map(int, input().split())

arr = [0] * N

for m in range(M):
  i, j, k = map(int, input().split())
  for num in range(i, j+1):
    arr[num-1] = k


print(*arr)