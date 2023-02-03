# Q4 Answer Template

def solution(arr):
    temp = 1
    maxvalue = 0
    
    for i in arr:
        temp *= i
        if i > maxvalue:
            maxvalue = i
    
    for j in range(maxvalue, temp + 1):
        flag = 0
        for a in arr:
            if j % a != 0:
                flag = 1
        if flag == 0:
            answer = j
            break
            
    return answer

# arr = [None]*15
arr = [2,6,8,14]
answer = solution(arr)
print(answer)