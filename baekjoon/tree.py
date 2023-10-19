import sys

N, M = map(int, sys.stdin.readline().split())
# M = list(int(sys.stdin.readline().split()))
trees = list(map(int,sys.stdin.readline().split()))

def sum_tree(heights, target_height):
    total_length = 0
    for height in heights:
        if height > target_height:
            total_length += height - target_height
    return total_length

def cutter(length, target_length):
    start = 0
    end = max(length)

    # result_height = 0
    while start <= end:
        mid = (start + end) // 2
        total_length = sum_tree(length, mid)
        if total_length >= target_length :
                start = mid +1   
                result = mid     
        else :
                end = mid -1   
    return result



print (cutter(trees, M))
