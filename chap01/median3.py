def med3(a,b,c):
    if a >=b:
        if b >= c:
            return b
        elif a <=c:
            return a
        else  :
            return c
        
    elif a>c :
        return a
    elif b<c :
        return b
    else :
        return c
    
print("숫자를 입력하세요")
a=int(input())
b=int(input())
c=int(input())
    
print(f"세 수의 중앙값은 {med3(a,b,c)} 입니다.")
