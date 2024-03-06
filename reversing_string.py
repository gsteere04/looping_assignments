def reverse_while(s: str) -> str:
    index = len(s) - 1
    rs = ""
    while index >= 0:
        rs += s[index]
        index -= 1
    return rs

def reverse_for(s: str) -> str:
    
    rs = ""
    for i in range(len(s)- 1, -1, -1):
        rs += s[i]
    return rs
#def reverse_for(s: str) -> str:

def reverse_foreach(s: str) -> str:
    rs = ""
    for char in s:
        rs += char + rs
    return rs

result = reverse_while("hello")
print(result)

result2 = reverse_for("hello")
print(result2)

result3 = reverse_foreach("hello")
print(result3)
