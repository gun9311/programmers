global_variable = 10

def modify_global_variable(): # global 키워드를 사용하여 전역 변수를 함수 내에서 사용하겠다고 선언
    global global_variable
    global_variable += 5

modify_global_variable()
print(global_variable)