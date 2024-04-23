
word = input().upper()  # 일단 대문자로 저장

num_list = [0] * 26  # 알파벳 개수(26개)만큼 리스트 만들기
max_num = 0  # 최댓값(가장 많이 쓰인 알파벳) 저장
max_list = []    # 최대값의 인덱스를 저장할 리스트 : 인덱스로 알파벳 찾을 수 있음



# 입력한 word에 있는 알파벳 각각의 개수를 아스키코드로 변환해서 각 번호에 맞게 숫자 증가
for w in word : 
  num_list[ord(w)-65] += 1

# 최대값 찾기
for num in num_list:
  if max_num < num:
    max_num = num

# 최대값이 여러 개인지 확인
for i in num_list :
  if i == max_num :
    max_list.append(i)

# 최대값이 한 개가 맞으면, 그 알파벳의 인덱스가 max_list[0]임. num_list에서 max_list[0] 에 해당하는 알파벳을 구하기 위해 65 더해서 chr로 바꿔줌
if len(max_list) == 1:
  # 
  print(chr(num_list.index(max_list[0]) + 65))
else:
  print('?')