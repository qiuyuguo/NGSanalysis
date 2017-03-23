inname = input('Differentially enriched peak to be analyzed:\n')
file = open(inname).readlines()
for i in range(len(file)):
    file[i] = file[i].rstrip('\n').split('\t')
#scale = input('scale of the desired peak regions: ')
#scale = int(scale)
record = []
position = []
for i in range(len(file)):
    record.append(file[i][0].strip('"')+'\t'+file[i][1]+'\t'+file[i][2])
    position.append(file[i][0].strip('"')+'\t'+str(int((int(file[i][1])+int(file[i][2]))/2))+'\t0')
outname = inname.strip('txt')+'bed'
out = open(outname,'w')
for i in range(len(record)):
    print(record[i],file=out)
out.close()
posname = inname.strip('txt')+'pos'
pos = open(posname,'w')
for i in range(len(record)):
    print(position[i],file=pos)
pos.close()
