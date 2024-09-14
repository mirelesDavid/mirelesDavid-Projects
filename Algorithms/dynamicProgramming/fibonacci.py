

def fibRecursive(n):
    if n <= 1:
        return n
    else:
        return fibRecursive(n-1) + fibRecursive(n-2)

def fibDynamic(n):
    sequence = []
    first, second = 0, 1
    while len(sequence) < n:
        sequence.append(first)
        first, second = second, first + second
    return sequence

print(fibDynamic(10000))

def fibMemo(n, memo):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibMemo(n-1, memo) + fibMemo(n-2, memo)
    return memo[n]
    
print("Memoization")
print(fibMemo(100, {}))

