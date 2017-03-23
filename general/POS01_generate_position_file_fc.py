in_name = input('QuEST out file name:\n')
file = open(in_name).readlines()
for i in range(len(file)):
    file[i] = file[i].split(' ')
record = []
for i in range(len(file)):
    if file[i][0][0] == 'P':
        record.append(file[i][0]+'\t'+file[i][1]+'\t'+file[i][2]+'\t'+file[i][4]+'\t'+file[i][6]+'\t'+file[i][10])
out = open(in_name.rstrip('.out.accepted')+'.txt','w')
for i in range(len(record)):
    print(record[i],file=out)
out.close()
