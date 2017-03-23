def union(after_merge,region2):
    region1=after_merge[len(after_merge)-1]
    if region1[1]==region2[1]:
        right=max(region1[3],region2[3])
        left=min(region1[2],region2[2])
        if right-left<(region1[3]-region1[2])+(region2[3]-region2[2]):
            merge=['merged',region1[1],left,right,'merged','merged']
            after_merge[len(after_merge)-1]=merge
            print('merging event!')
        else:
            after_merge.append(region2)
    else:
        after_merge.append(region2)

RR=open('mm9.GREAT3.0.definite.regulatory_domains.500kb.txt').readlines()
for i in range(len(RR)):
    RR[i]=RR[i].rstrip('\n').split('\t')
    RR[i][2]=int(RR[i][2]);
    RR[i][3]=int(RR[i][3]);
from operator import itemgetter
RR=sorted(RR,key=itemgetter(0))

in_name=input('Please input genes list whose dRR will be extracted:\n')
genes=open(in_name).readlines()
for i in range(len(genes)):
    genes[i]=genes[i].rstrip('\n').split('\t')
    genes[i][0]=genes[i][0].strip('"')

ensembl=open('ensemblID2GeneSymbol.txt').readlines()
for i in range(len(ensembl)):
    ensembl[i]=ensembl[i].rstrip('\n').split('\t')
ensembl=sorted(ensembl,key=itemgetter(1))

for i in range(len(genes)):
    
    target=genes[i][0]    
    
    start=0
    end=len(ensembl)-1
    find=False
    while start+1<end:
        mid=start+int((end-start)/2)
        if ensembl[mid][1]<target:
            start=mid
        elif ensembl[mid][1]>target:
            end=mid
        else:
            loc=mid
            find=True
            break
    if find == False:
        if ensembl[start][1]==target:
            loc=start
        elif ensembl[end][1]==target:
            loc=end
        else:
            print('1st round unmatched gene '+target)
            continue
    genes[i][0]=ensembl[loc][0]

result=[]
for i in range(len(genes)):
    
    target=genes[i][0]    
    
    start=0
    end=len(RR)-1
    find=False
    while start+1<end:
        mid=start+int((end-start)/2)
        if RR[mid][0]<target:
            start=mid
        elif RR[mid][0]>target:
            end=mid
        else:
            loc=mid
            find=True
            break
    if find == False:
        if RR[start][0]==target:
            loc=start
        elif RR[end][0]==target:
            loc=end
        else:
            print('unmatched gene '+target)
            continue
    result.append(RR[loc])

from operator import itemgetter
result=sorted(result,key=itemgetter(1,2))
result_union=[result[0]]
for i in range(1,len(result)):
    union(result_union,result[i])

total_cover=0
for i in range(len(result_union)):
    coverage=int(result_union[i][3])-int(result_union[i][2])
    total_cover=total_cover+coverage
print(total_cover)

for i in range(1,len(result_union)):
    if result_union[i][1] == result_union[i-1][1]:
        if result_union[i][2] <= result_union[i-1][3]:
            print('conflict at line '+str(i+1))
            print(result_union[i-1])
            print(result_union[i])
        
out_name=input('Please specify output file name:\n')
out=open(out_name,'w')
for i in range(len(result_union)):
    print(''.join(str(result_union[i][j])+'\t' for j in range(len(result[i]))).rstrip('\t'),file=out)
out.close()
