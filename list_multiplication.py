def list_multiply_while(a: list[int], b: list[int]) -> list[int]:
    i = 0
    result_list = []
    while i< len(a) and i < len(b):
        result = a[i] * b[i]
        result_list.append(result)
        i += 1
    return result_list

#Used ChatGPT to help condense the "for i in range".  All code was written by me though, only change made by chatGPT was implementing the "min".
def list_multiply_for(a: list[int], b: list[int]) -> list[int]:
    result_list = []
    for i in range(min(len(a), len(b))):
        result = a[i] * b[i]
        result_list.append(result)
    return result_list

a = [1, 2, 3]
b = [4, 5, 6]

a2 = [11, 19, 32]
b2 = [10, 45, 9]
result = list_multiply_while(a, b)
print()
print("While loop: ")
print(result)
print()

result2= list_multiply_for(a2, b2)
print()
print("For loop: ")
print(result2)
print()




 