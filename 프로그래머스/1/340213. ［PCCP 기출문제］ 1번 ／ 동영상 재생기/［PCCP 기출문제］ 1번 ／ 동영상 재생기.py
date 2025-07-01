def solution(video_len, pos, op_start, op_end, commands):
    
    # 전부 초 단위로 바꿔줌
    l = [video_len, pos, op_start, op_end]
    for i in range(4):
        l[i] = int(l[i][:2])*60 + int(l[i][3:])
    
    # 오프닝 구간인지 확인
    if l[2] <= l[1] <= l[3]:
        l[1] = l[3]
    
    for com in commands:
        l[1] = command(com, l)
        
        # 오프닝 구간인지 확인
        if l[2] <= l[1] <= l[3]:
            l[1] = l[3]
    
    min = str(l[1]//60) if (l[1]//60)>=10 else "0"+str(l[1]//60)
    sec = str(l[1]%60) if (l[1]%60)>=10 else "0"+str(l[1]%60)
    
    return min + ":" + sec

def command(c, time_list):
    if c=="prev":
        time_list[1] -= 10
    elif c=="next":
        time_list[1] += 10
    
    if time_list[1]<0:
        time_list[1] = 0
    elif time_list[1]>time_list[0]:
        time_list[1] = time_list[0]    
    
    return time_list[1]