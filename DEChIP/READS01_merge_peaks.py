# merge peaks within 150 bp from each other
import os
os.chdir('/Users/qiuyuguo/Dropbox/work/01_project_bcat/analysis/ChIP-Seq')

inName=input('concatenated file to merge:\n')
cons=open(inName).readlines()
for i in range(len(cons)):
    cons[i]=cons[i].rstrip('\n').split('\t')

for i in range(len(cons)):
    cons[i][1]=int(cons[i][1])
    cons[i][2]=int(cons[i][2])

from operator import itemgetter
cons=sorted(cons,key=itemgetter(0,1))
trim=[]
i=1
while i<len(cons)-1:
    #print(i)
    pool=[cons[i]]
    for j in range(i+1,len(cons)):
        if cons[j][0]==cons[j-1][0]:
            if cons[j][1]<cons[j-1][2]:
                pool.append(cons[j])
            else:
                start=pool[0][1]
                end=pool[len(pool)-1][2]
#                sig=[]
#                for k in range(3,len(cons[0])):
#                    sig.append(sum([pool[x][k] for x in range(len(pool))])/len(pool))
                peak=[cons[i][0],start,end]
#                for k in range(len(sig)):
#                    peak.append(sig[k])
                trim.append(peak)
                i=j+1
                break
        else:
            if j==i+1:
                trim.append(cons[i])
                i=j+1
                break
            else:
                start=pool[0][1]
                end=pool[len(pool)-1][2]
#                sig=[]
#                for k in range(3,len(cons[0])):
#                    sig.append(sum([pool[x][k] for x in range(len(pool))])/len(pool))
                peak=[cons[i][0],start,end]
#                for k in range(len(sig)):
#                    peak.append(sig[k])
                trim.append(peak)
                i=j+1
                break 

out=open(inName.rstrip('bed')+'m.bed','w')
for i in range(len(trim)):
    center=int((trim[i][1]+trim[i][2])/2)
    trim[i][1]=center-75
    trim[i][2]=center+75
    out.write(''.join(str(trim[i][j])+'\t' for j in range(3)).rstrip('\t')+'\n')
out.close()
