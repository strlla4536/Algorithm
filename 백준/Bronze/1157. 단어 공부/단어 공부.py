ans = input().upper() #upper함수를 쓰자!!!
uni = list(set(ans))
cnt_list = []
for u in uni:
    num = ans.count(u)
    cnt_list.append(num)

M = max(cnt_list)
if cnt_list.count(M) > 1:
    print("?")
else : 
    idx = cnt_list.index(M)
    print(uni[idx])