s = input()

ans_list = [-1] * 26

for i in range(len(s)):
  pos = ord(s[i]) - 97
  if ans_list[pos] == -1:
    ans_list[pos] = i

print(*ans_list)