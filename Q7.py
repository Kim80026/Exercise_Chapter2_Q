# Q7 Answer Template

def solution(arr):
    answer = []
    temp = arr[0]
    answer.append(temp)
    
    for tmp in arr:
        if tmp != temp:
            temp = tmp
            answer.append(temp)
            
            
    return answer

arr = [1,1,3,3,0,1,1]
#arr = [4,4,4,3,3]
answer = solution(arr)
print(answer)