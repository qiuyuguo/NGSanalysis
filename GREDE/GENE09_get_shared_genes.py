inname1=input('input GREAT gene-peak association file 1:\n')
file1=open(inname1).readlines()
for i in range(len(file1)):
    file1[i]=file1[i].rstrip('\n').split('\t')
inname2=input('input GREAT gene-peak association file 2:\n')
file2=open(inname2).readlines()
for i in range(len(file2)):
    file2[i]=file2[i].rstrip('\n').split('\t')
result=[]
for i in range(len(file1)):
    for j in range(len(file2)):
        if file1[i][0].strip('"').upper()==file2[j][0].strip('"').upper():
            result.append(file1[i])
            break
print('Number of shared genes:')
print(len(result))
out=open(inname1.rstrip('txt')+'sharedby.'+inname2,'w')
for i in range(len(result)):
    print(''.join(result[i][j]+'\t' for j in range(len(result[i]))).rstrip('\t'),file=out)
out.close()
    
