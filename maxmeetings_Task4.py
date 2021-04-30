#Task4

def maxMeetings(Arr,n):
    meets=[]
    Arr.sort(key = lambda x : x[1]) 
    
    meets.append(Arr[0][2]) 
    check_time = Arr[0][1]
    
    for i in range(1, n):
        if Arr[i][0] > check_time:
            meets.append(Arr[i][2])
            check_time = Arr[i][1]
    return (len(meets))    

s = [ 75270, 50074, 43659, 8931, 11273, 27545, 50879, 77924 ]
f = [ 112960, 114515, 81825, 93424, 54316, 35533, 73383, 160252]
Arr = []
n=len(s)
for i in range(n):
        Arr.append([s[i], f[i], i])

maxm = maxMeetings(Arr,n)
print(maxm)

