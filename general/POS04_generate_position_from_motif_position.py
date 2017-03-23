inname = input('motif file to be analyzed:\n')
file = open(inname).readlines()
for i in range(len(file)):
    file[i] = file[i].split()
#scale = input('scale of the desired peak regions: ')
#scale = int(scale)
scale = 100
record = []
for i in range(len(file)):
    record.append(['P'+str(i),file[i][0],file[i][1]])
outname = inname.strip('txt')+'pos.txt'
out = open(outname,'w')
for i in range(len(record)):
    print(''.join(record[i][j]+'\t' for j in range(len(record[i]))).rstrip('\t'),file=out)
out.close()
