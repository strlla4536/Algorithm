def solution(s):    
    stack = []
    
    for char in s:
        if stack and char == stack[-1]:
            stack.pop()
        else:
            stack.append(char)
    
    return 1 if not stack else 0
        
