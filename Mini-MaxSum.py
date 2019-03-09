a=list(map(int,input().split()))
sum=0
minsum=0
maxsum=0
mini=min(a)
maxi=max(a)
for i in range(0,5):
    sum+=a[i]
minsum=sum-maxi
maxsum=sum-mini
print(minsum,maxsum)        


