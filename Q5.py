# Q5 Answer template
def solution(n, s):
    temp = []
    for i in range(1, s//2 + 1):
        temp.append([i, s - i])
    
    if len(temp) == 0:
        return -1
    
    tmp = float('-inf')
    
    for a, b in temp:
        if a * b > tmp:
            answer = [a, b]

    return answer

n = 2
s = 8
answer = solution(n, s)
print(answer)