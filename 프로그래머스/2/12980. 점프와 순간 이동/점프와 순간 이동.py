def solution(n):
    # n : 이동하려는 거리, return : 건전지 사용량 최소값
    battery = 0
    
    while n>0:
        if n%2 == 0:
            n = n//2
        else:
            n-=1
            battery+=1
    

    return battery