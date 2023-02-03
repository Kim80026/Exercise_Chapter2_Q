# Q6 Answer template

def solution(arr):
    li = arr.copy()
    minvalue = min(li)
    li.remove(minvalue)
    
    if len(li) == 0:
        li.append(-1)
        
    return li

def solution2(arr):
    li = arr.copy()
    minvalue = float('inf')
    
    for i in li:
        if i < minvalue:
            minvalue = i
            
    li.remove(minvalue)
    
    if len(li) == 0:
        li.append(-1)
        
    return li

arr = [4, 3, 2, 1]
answer = solution(arr)
answer2 = solution2(arr)
print(answer)
print(answer2)