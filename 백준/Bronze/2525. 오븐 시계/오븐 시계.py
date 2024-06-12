h, m = map(int, input().split())
time = int(input())

m += time 

if m >= 60:
  h += m //60
  h = h % 24
  m = m % 60
  
print(h, m)