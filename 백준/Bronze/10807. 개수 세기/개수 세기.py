import sys
input = sys.stdin.readline

n = int(input())
l= list(map(int,input().split()))
v = int(input())

cnt = 0 

for i in range(len(l)):
  if l[i] == v:
    cnt += 1
  else:
    pass

print(cnt)