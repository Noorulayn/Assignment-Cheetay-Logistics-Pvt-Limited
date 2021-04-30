#Task2

def equilibriumPoint(A = [], n=0):
    if n == 1:
        return 1
    else:
        x = None
        for y in range(1, len(A)):
            if sum(A[0:y]) == sum(A[y+1:]):
              x=y+1
              return x
        if x==None:
            return -1
                      
a = [1,3,5,2,2]
eq = equilibriumPoint(a, len(a))
print(eq)
