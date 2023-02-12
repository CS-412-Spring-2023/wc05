import random
def algo_A(n: int):
    ''' Runs in \Theta(n^2) time
    '''
    random_number = random.randint(1, n*100)
    sum = 0
    for i in range(n):
        for j in range(n):
            sum += j
            if sum == random_number:
                return True
            
    return False

def algo_B(n: int):
    
    check = random.randint(1, n*10)
    a = 0
    while (a <= n**2):
        if (check == a):
            return a
        a += 1
        
    return a
    

def algo_C(n: int):
    
    array = []
    
    for i in range (n):
        array.append(random.randint(1, n*10))
        
    low = 0
    high = len(array) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if array[mid] == n:
            return mid
        elif array[mid] < n:
            low = mid + 1
        else:
            high = mid - 1
    
    return -1


def algo_D(n: int):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 1
    
    f = [0] * (n + 1)
    f[1] = 1
    f[2] = 1
    for i in range(3, n + 1):
        f[i] = f[i - 1] + f[i - 2]
    
    return f[n]
