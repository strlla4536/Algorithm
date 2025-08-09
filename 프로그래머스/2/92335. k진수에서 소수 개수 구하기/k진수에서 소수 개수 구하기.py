def to_base_k(n, k):
    if n == 0:
        return "0"
    
    digits = []
    
    while n > 0:
        digits.append(str(n % k))
        n //= k
    
    return ''.join(digits[::-1])

def is_prime(num):
    if num == 1:
        return False
    elif num == 2:
        return True
    else:
        for i in range(3, int(num**0.5)+1):
            if num % i == 0:
                return False
    return True


def solution(n, k):
    k_num = to_base_k(n,k)
    
    candidates = k_num.split('0')
    count = 0
    for candidate in candidates:
        if candidate == '':
            continue
        if '0' in candidate:
            continue
        if is_prime(int(candidate)):
            count += 1

    return count