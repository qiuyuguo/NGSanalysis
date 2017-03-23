print('now process the bed file before extension to grab the ATAC peak centers.')
bedName=input('bed file to be processed:\n')
bed=open(bedName).readlines()
for i in range(len(bed)):
    bed[i]=bed[i].rstrip('\n').split('\t')

header = []
peak = []
for i in range(len(bed)):
    bed[i].append('ID=ATAC'+str(i))

from operator import itemgetter
bed = sorted(bed,key=itemgetter(3))

for i in range(len(bed)):
    header.append(bed[i][0:3])
    peak.append([bed[i][3],bed[i][0],bed[i][1],bed[i][2],'+'])

outName=bedName.rstrip('bed')+'header'
out=open(outName,'w')
for i in range(len(header)):
    print(''.join(str(header[i][j])+'\t' for j in range(len(header[i]))).rstrip('\t'),file=out)
out.close()

peakName=bedName.rstrip('bed')+'peak'
peakout=open(peakName,'w')
for i in range(len(peak)):
    print(''.join(str(peak[i][j])+'\t' for j in range(len(peak[i]))).rstrip('\t'),file=peakout)
peakout.close()
