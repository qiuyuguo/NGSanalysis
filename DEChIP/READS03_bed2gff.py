bedName=input('bed file to be converted:\n')
bed=open(bedName).readlines()
for i in range(len(bed)):
    bed[i]=bed[i].rstrip('\n').split('\t')
gff=[]
for i in range(len(bed)):
    line = [bed[i][0],'ATAC','exon',bed[i][1],bed[i][2],'.','+','.','ID=ATAC'+str(i)]
    gff.append(line)
from operator import itemgetter
gff = sorted(gff,key=itemgetter(8))
outName=bedName.rstrip('bed')+'gff'
out=open(outName,'w')
for i in range(len(gff)):
    print(''.join(str(gff[i][j])+'\t' for j in range(len(gff[i]))).rstrip('\t'),file=out)
out.close()
outName=bedName.rstrip('bed')+'header'
