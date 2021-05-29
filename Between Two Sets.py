# solution1
def getTotalX(a, b):
    
    # Write your code here
    count = 0
    max_a = max(a)
    max_b = max(b)
    for num in range(max_a, max_b+1):
        con1 = all([num%i==0 for i in a])
        con2 = all([j%num==0 for j in b])
        count += con1*con2
    return count
    
# solution2
def getTotalX(a, b):
    
    # Write your code here
    count = 0
    max_a = max(a)
    max_b = max(b)
    for num in range(max_a, max_b+1):
        con1 = 0
        con2 = 0
        for i in a:
            if num%i == 0:
                con1 += 1
        for i in b:
            if i%num == 0:
                con2 += 1
        if con1 + con2 == (n + m):
            count +=1
    return count
