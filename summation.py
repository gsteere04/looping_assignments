def summation_while(n):
    total = 0
    g = 1 
    while g <=  n:
        total += g
        g += 1

    return total
print(summation_while(10))

def summation_for(n):
    total = 0
    g = 1
    for i in range(n):
        total += g
        g += 1
    return total
print(summation_for(12))
        
