def solution(wallet, bill):
    ans = 0
    
    while min(bill)>min(wallet) or max(bill)>max(wallet):
        print("전: ", bill)
        if bill[0] >= bill[1]:
            bill[0] = bill[0]//2
        else:
            bill[1] = bill[1]//2
        print("후: ", bill)
        
        ans += 1
    return ans