import sys
input = sys.stdin.readline

arr = [0] * 43

for _ in range(10):
  r = int(input()) % 42
  arr[r] += 1

ans = [i for i in arr if i != 0]
print(len(ans))