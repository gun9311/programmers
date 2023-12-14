def solution(record):
    answer = []
    real_name = {}
    for i in record:
        if "Leave" in i :
            status, identy = i.split()
        else :
            status, identy, name = i.split()
            real_name[identy] = name
            print(real_name)
    for i in record:
        if "Enter" in i:
            status, identy, name = i.split()
            answer.append(real_name[identy] + "님이 들어왔습니다.")
        elif "Leave" in i:
            status, identy = i.split()
            answer.append(real_name[identy] + "님이 나갔습니다.")
    return answer