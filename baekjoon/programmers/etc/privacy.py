def solution(today, terms, privacies):
    d={}
    answer = []
    year, month, day = map(int,today.split('.'))
    today_total = 12*28*year + 28*month + day
    for term in terms :
        term_k, term_t = term.split()
        for idx, privacy in enumerate(privacies) :
            if term_k in privacy :
                p_date, p_kind = privacy.split()
                y,m,d = map(int,p_date.split('.'))
                p_total = 12*28*y+28*m+d
                if p_total + 28*int(term_t) <= today_total :
                    answer.append(idx+1)
    answer.sort()
    return answer

today = "2022.05.19"
terms = ["A 6", "B 12", "C 3"]
pri = ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]
solution(today,terms,pri)