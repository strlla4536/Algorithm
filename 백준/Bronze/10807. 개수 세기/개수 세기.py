import sys
input = sys.stdin.readline

n = int(input())
l= list(map(int,input().split()))
v = int(input())
print(l.count(v))