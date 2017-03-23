print('This is to process fimo output txt file using fa file from extract_sequence_chunks_near_sites script.')
inname=input('name of the fimo output file:\n')
file=open(inname).readlines()
motif=[]
for i in range(1,len(file)):
    file[i]=file[i].rstrip('\n').split('\t')
    file[i][1]=file[i][1].split('_')
    middle=int((int(file[i][2])+int(file[i][3]))/2)
    pos=int(file[i][1][1])-100+middle
    motif.append([file[i][1][0],pos,middle,file[i][4],file[i][6],file[i][8]])
    file[i][1]=''.join(file[i][1][j]+'_' for j in range(len(file[i][1]))).rstrip('_')
from operator import itemgetter
file=sorted(file,key=itemgetter(1))
peak=[]
count=1
for i in range(1,len(file)-1):
    if file[i][1]==file[i-1][1]:
        count=count+1
    else:
        peak.append([file[i-1][1],str(count)])
        count=1              
if i==len(file):
    if file[i][1]==file[i-1][1]:
        count=count+1
        peak.append([file[i-1][1],str(count)])
    else:
        peak.append([file[i][1],str(count)])
outname=inname.strip('txt')+'motif.txt'
out=open(outname,'w')
for i in range(len(motif)):
    print(''.join(str(motif[i][j])+'\t' for j in range(len(motif[i]))).rstrip('\t'),file=out)
out.close()
outname2=inname.strip('txt')+'summary.txt'
out2=open(outname2,'w')
for i in range(len(peak)):
    print(''.join(str(peak[i][j])+'\t' for j in range(len(peak[i]))).rstrip('\t'),file=out2)
out2.close()
