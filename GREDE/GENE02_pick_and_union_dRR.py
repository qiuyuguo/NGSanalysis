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

in_name=input('Please input genes list whose dRR will be extracted:\n')
gene=open(in_name).readlines()
result=[]
for i in range(len(gene)):
    gene[i]=gene[i].rstrip('\n').split('\t')
    for j in range(len(RR)):
        if gene[i][0].strip('"')==RR[j][5]:
            result.append(RR[j])

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
