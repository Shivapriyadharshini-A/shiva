def longSubSeq(str1, str2):  
    l1 = len(str1) 
    l2 = len(str2)
    DP = [[None]*(l2+1) for i in range(l1+1)]
    substr=""
    for i in range(l1 + 1): 
        for j in range(l2 + 1): 
            if i == 0 or j == 0 : 
                DP[i][j] = 0
            elif str1[i-1] == str2[j-1]: 
                DP[i][j] = DP[i-1][j-1]+1
                substr+=str1[i-1]
            else: 
                DP[i][j] = max(DP[i-1][j], DP[i][j-1]) 
    return DP[l1][l2],(substr) 

str1=input().strip()
str2=input().strip()
x,y=longSubSeq(str1,str2)
print(x,''.join(set(y)))
