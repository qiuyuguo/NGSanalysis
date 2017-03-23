print('Now calculate number of peaks located within regulatory regions of genes from GREAT output.')
great_name=input('GREAT output file:\n')
great=open(great_name).readlines()
for i in range(len(great)-1):
    great[i]=great[i].strip('\n').split('\t')
    great[i][1]=great[i][1].split(', ')
from operator import itemgetter
great=sorted(great,key=itemgetter(0))
result=[]
import math
for i in range(1,len(great)):
    record=[]
    SUM=0
    for j in range(len(great[i][1])):
        great[i][1][j]=great[i][1][j].split(' ')
        distance=int(great[i][1][j][1].lstrip('(').rstrip(')'))
        intensity=great[i][1][j][0].split('.')[1]
        peak=great[i][1][j][0].split('.')[0]
        record.append([peak,distance,intensity])
        score=float(intensity)/math.pow(max(abs(distance),20000),0.1)
        SUM=SUM+score
    record=sorted(record,key=itemgetter(2))
    r=''.join(str(record[x][0])+','+str(record[x][1])+','+record[x][2]+';' for x in range(len(record)))
    result.append(''.join(great[i][0]+'\t'+r+'\t'+str(len(great[i][1]))+'\t'+str(round(SUM))))
outname=great_name.strip('txt')+'hits.txt'
out=open(outname,'w')
for i in range(len(result)):
    print(result[i],file=out)
out.close()

