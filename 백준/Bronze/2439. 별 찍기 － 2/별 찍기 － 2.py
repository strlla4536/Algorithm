import sys
input = sys.stdin.readline

t = int(input())

for i in range(1,t+1):
  print(" "*(t-i),end='*'*i)
  if i!=t:
    print()