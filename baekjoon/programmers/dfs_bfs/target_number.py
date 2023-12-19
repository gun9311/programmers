def solution(numbers, target):
    answer = 0
    
    def dfs(n,result):
        nonlocal answer
        if n == len(numbers):
            if result == target :
                answer += 1
                return
        else :
            now = numbers[n]
            next = n+1
            dfs(next,result+now)
            dfs(next,result-now)
        
    result = 0
    dfs(0,result)
    print(answer)
    return answer
n = [4, 1, 2, 1]
t = 4
solution(n,t)