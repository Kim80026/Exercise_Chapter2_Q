# Q1 Answer template
rank = {6 : 1, 5 : 2, 4 : 3, 3 : 4, 2 : 5, 1 : 6, 0 : 6}

def solution(lottos, win_nums):
    zero = lottos.count(0)
    win = 0
    
    for lotto in lottos:
        if lotto in win_nums:
            win += 1
    
    max_, min_ = win + zero, win
    answer = [rank[max_], rank[min_]]
    
    return answer

lottos = [44, 1, 0, 0, 31, 25]
win_nums = [31, 10, 45, 1, 6, 19]
answer = solution(lottos, win_nums)
print(answer)