inname = input('peak file to be analyzed:\n')
file = open(inname).readlines()
for i in range(len(file)):
    file[i] = file[i].split()
#scale = input('scale of the desired peak regions: ')
#scale = int(scale)
scale = 150
record = []
for i in range(len(file)):
    record.append(file[i][1]+'\t'+str(int(file[i][2])-int(scale/2))+'\t'+str(int(file[i][2])+int(scale/2))+'\t'+file[i][0]+'.'+str(int(float(file[i][3]))))
outname = inname.strip('txt')+str(scale)+'.bed'
out = open(outname,'w')
for i in range(len(record)):
    print(record[i],file=out)
out.close()
