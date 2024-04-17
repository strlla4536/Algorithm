# 알파벳 문자열 만들고 문자열에 있으면 인덱스로 접근해서 출력
s = list(input())
alphabets = 'abcdefghijklmnopqrstuvwxyz'

for i in alphabets :
  if i in s:
    print(s.index(i), end=' ')

  else:
    print(-1, end=' ')

