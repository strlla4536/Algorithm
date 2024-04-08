import sys
input = sys.stdin.readline

max_val = 0
val = 0
num = 0

for i in range(9):
  val = int(input())
  if max_val < val:
    max_val = val
    num = i+1

print(f"{max_val}\n{num}")