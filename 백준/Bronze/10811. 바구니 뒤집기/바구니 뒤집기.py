import sys
input = sys.stdin.readline

n, m = map(int,input().split())
arr = [i for i in range(n)]


for _ in range(m):
  i, j = map(int, input().split())

  tmp = arr[i-1:j]
  tmp.reverse()
  arr[i-1:j] = tmp

for a in arr:
  print(a+1, end = ' ')