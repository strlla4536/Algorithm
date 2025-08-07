def solution(data, ext, val_ext, sort_by):
    answer = []
    by = ["code", "date", "maximum", "remain"]
    
    for i in range(len(data)):
        if data[i][by.index(ext)] < val_ext:
            answer.append(data[i])
    
    answer.sort(key = lambda x: x[by.index(sort_by)])
    
    return answer