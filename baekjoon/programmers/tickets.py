def solution(tickets):
    answer = ["ICN"]
    visited = [False]*len(tickets)
    
    def dfs(i, start, t):
        visited[i] = True
        answer.append(start[1])
        t -= 1
        if t == 0 :
            return
        for idx,ticket in enumerate(tickets) :
            if visited[idx] == False and ticket[0] == start[1] :
                dfs(idx,ticket,t)
    
    tickets.sort(key= lambda x: x[1])
    for idx,ticket in enumerate(tickets) :
        T = len(tickets)
        if ticket[0] == "ICN":
            dfs(idx,ticket,T)
            if len(answer) == T+1 :
                print(answer)
                return answer

t =[["ICN", "BOO"], ["ICN", "COO"], ["COO", "DOO"], ["DOO", "COO"], ["BOO", "DOO"], ["DOO", "BOO"], ["BOO", "ICN"], ["COO", "BOO"]]
solution(t)