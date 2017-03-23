print('Extend region boundary in bed file.')
in_name=input('input bed file:\n')
in_bed=open(in_name).readlines()
for i in range(len(in_bed)):
    in_bed[i]=in_bed[i].rstrip('\n').split('\t')
    in_bed[i][1]=int(in_bed[i][1])
    in_bed[i][2]=int(in_bed[i][2])
ext=input('radius of the new range.\n')
ext=int(ext)
from operator import itemgetter
in_bed=sorted(in_bed,key=itemgetter(0,1))
for i in range(len(in_bed)):
    mid=int((in_bed[i][1]+in_bed[i][2])/2)
    in_bed[i][1]=mid-ext
    in_bed[i][2]=mid+ext
count=0
for i in range(1,len(in_bed)):
    if in_bed[i][0] == in_bed[i-1][0]:
        if in_bed[i][1] <= in_bed[i-1][2]:
            mid=int((in_bed[i-1][2]+in_bed[i][1])/2)
            in_bed[i-1][2]=mid-1
            in_bed[i][1]=mid
            count+=1
    in_bed[i].append('ID=ATAC'+str(i))
print('number of overlapping events:')
print(count)
out_name=in_name.rstrip('bed')+str(ext)+'.bed'
out=open(out_name,'w')
for i in range(len(in_bed)):
    print(''.join(str(in_bed[i][j])+'\t' for j in range(len(in_bed[i]))).rstrip('\t'),file=out)
out.close()
