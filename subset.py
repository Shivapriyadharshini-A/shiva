import itertools
def findsubset(arr,length):
    return set(itertools.combinations(arr,length))

    
def subset(arr,total):
    cnt=0
    result=[]
    if total in arr:
        cnt+=1
    else:
        itr=2
        if len(arr)>1:
            while(itr!=len(arr)):
                for s in findsubset(arr,itr):
                    if sum(s)==total:
                        cnt+=1
                        result.append(s)
                itr+=1
    return result,cnt
array=list(map(int,input().split()))
total=int(input())
l=len(array)
x,y=subset(array,total)
print(x,y)
