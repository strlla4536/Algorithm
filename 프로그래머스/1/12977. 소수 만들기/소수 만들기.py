import math

def is_prime_number(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n%i==0: # 나누어 떨어지면
            return False
    return True
    

def solution(nums):
    answer = 0
    
    for i in range(len(nums)-2):
        for j in range(i+1, len(nums)-1):
            for k in range(j+1, len(nums)):
                if is_prime_number(nums[i]+nums[j]+nums[k]):
                    answer+=1
    
    return answer


    
    