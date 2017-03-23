peak_name=input('Please input peak list which will be hitting the RR:\n')
peak=open(peak_name).readlines()
for i in range(len(peak)):
    peak[i]=peak[i].rstrip('\n').split('\t')
    peak[i][2]=int(peak[i][2])

RR_name=input('Target RR:\n')
RR=open(RR_name).readlines()
for i in range(len(RR)):
    RR[i]=RR[i].rstrip('\n').split('\t')
    RR[i][2]=int(RR[i][2])
    RR[i][3]=int(RR[i][3])

result=[]    
for i in range(len(peak)):
    for j in range(len(RR)):
        if peak[i][1]==RR[j][1]:
            if peak[i][2]>RR[j][2] and peak[i][2]<RR[j][3]:
                peak[i].append(RR[j][5])
                result.append(peak[i])
                break

from operator import itemgetter
result=sorted(result,key=itemgetter(1,2))
for i in range(1,len(result)):
    if result[i] == result[i-1]:
        print('repetitive picking')

print('observed hits: ',len(result))

total_cover=0
for i in range(len(RR)):
    coverage=int(RR[i][3])-int(RR[i][2])
    total_cover=total_cover+coverage
print('total coverage: ',total_cover)
mm9_size=2725765481
expect=round(len(peak)*total_cover/mm9_size,2)
print('expected hits: ',expect)

out_name=peak_name.rstrip('txt')+'in.'+RR_name
out=open(out_name,'w')
for i in range(len(result)):
    print(''.join(str(result[i][j])+'\t' for j in range(len(result[i]))).rstrip('\t'),file=out)
out.close()
