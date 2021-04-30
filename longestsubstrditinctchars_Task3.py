#Task3

def longestSubstrDitinctChars(s):
    if len(s)==0:
        return 0
    else:
        strdict = []
        strhist=[]
        for val in s:
            if val not in strdict:
                strdict.append(val)
            else:
                strhist.append(''.join(strdict))
                del strdict[:]
                strdict.append(val)
        strhist.append(''.join(strdict))        
        return max(map(len, strhist))

s = "geeksforgeeks"
lon = longestSubstrDitinctChars(s)
print(lon)
