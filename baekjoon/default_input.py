# def set_open(input_):
#     class open:
#         def __init__(self, x):
#             self.read = lambda: input_
#         def __iter__(self):
#             return iter(input_.split("\n"))
#     return open
# def set_input(input_):
#     return iter(input_.split("\n")).__next__
# input = set_input('''3''')

N = int(input())
print(2**N -1)


def hanoi(N,start,to,via):
     if N == 1 :
        print(start,to)

        return
     
     hanoi(N-1,start,via,to)
     print(start,to)
     hanoi(N-1,via,to,start)

if N <= 20 :
    hanoi(N,1,3,2)
     

        