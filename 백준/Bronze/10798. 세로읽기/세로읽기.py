l = [input() for _ in range(5)]

ans = ""

for str in range(15):
  for row in range(5):
    if len(l[row])>str:
      ans += l[row][str]
    else:
      pass
    
print(ans)