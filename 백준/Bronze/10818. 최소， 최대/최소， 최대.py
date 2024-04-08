import sys
input = sys.stdin.readline

n = int(input())

l = list(map(int, input().split()))
l_max = l[0]
l_min = l[0]

for i in l:
  if i > l_max:
    l_max = i
  elif i < l_min:
    l_min = i

print(f"{l_min} {l_max}")