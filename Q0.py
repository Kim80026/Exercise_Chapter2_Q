# Q0 Answer template
def minvalue(data, key):
    temp = []
    for i in data:
        if i < key:
            temp.append(i)
    return temp

N, X = map(int, input().split())  # N, X 를 입력받음

data = list(map(int, input().split())) # 리스트를 입력받음

answer = minvalue(data, X)
print(*answer)