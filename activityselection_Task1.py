
#Task1
def activityselection(start , end, N):
    #actlist = [0]
    x = 0
    count=1
    for y in range(1,N):
        if start[y] >= end[x]: 
            #actlist.append(y)
            x = y
            count+=1
    return (count)
 
start=[1,3,2,5]
end=[2,4,3,6]
act=activityselection(start , end, len(start))
print(act)
