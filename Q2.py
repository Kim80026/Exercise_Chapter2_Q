# Q2 Answer template

def solution(numbers):
    answer = 0
    for i in range(0, 10):
        if i not in numbers:
            answer += i
    return answer

def solution2(numbers):
    ans = 0
    tmp = 0
    for i in range(0, 10):
        ans += i
    
    for j in numbers:
        tmp += j
    
    return ans - tmp

numbers = [1,2,3,4,6,7,8,0]
answer = solution(numbers)
answer2 = solution2(numbers)
print(answer)
print(answer2)