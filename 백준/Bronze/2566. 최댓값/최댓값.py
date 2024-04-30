li = [list(map(int, input().split())) for _ in range(9)]

ans = 0
max_row, max_col = 0, 0

for row in range(9):
  for col in range(9):
    if li[row][col] >= ans :
      ans = li[row][col]
      max_row = row + 1
      max_col = col + 1

print(ans)
print(max_row, max_col)