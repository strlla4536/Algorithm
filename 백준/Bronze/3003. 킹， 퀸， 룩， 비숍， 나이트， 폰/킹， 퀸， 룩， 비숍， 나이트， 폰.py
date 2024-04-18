import sys
input = sys.stdin.readline

pieces = [1,1,2,2,2,8]
found = list(map(int,input().split()))

for i in range(6):
  pieces[i] = pieces[i] - found[i]

print(*pieces)