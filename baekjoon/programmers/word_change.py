from collections import deque
def solution(begin, target, words):
    answer = 0
    possible = deque()
    visited = [False]*(len(words)+1)
    
    def test(a,b):
        tmp = 0
        # if len(a) != len(b):
        #     print(error)
        #     return False
        for i in range(len(a)):
            if a[i] !=b[i]:
                tmp+=1
        if tmp ==1:
            return True
        else:
            return False 
    
    def search() :
        while possible :
            now, time = possible.popleft()
            if words[now] == begin :
                return time
            for i in range(len(words)):
                if visited[i] == False :
                    if test(words[now],words[i]) :
                    # check = set()
                    # for j in range(len(words[0])):
                        # check.add(words[now][j])
                        # check.add(words[i][j])
                    # if len(check) == len(words[0])+1:
                        possible.append((i,time+1))
    
    if target in words :
        words.append(begin)
        start = words.index(target)
        possible.append((start,0))
        visited[start] = True
        answer = search()
    print(answer)
    return answer

b = "aab"
t = "aba"
w =["abb", "aba"]
solution(b,t,w)