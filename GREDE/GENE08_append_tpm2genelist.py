genes_name=input('genes list to be analyzed:\n')
genes=open(genes_name).readlines()
for i in range(len(genes)):
    genes[i]=genes[i].rstrip('\n').split('\t')
    
print('Attaching tpm values from the 4 samples to the identified genes...')
tpm=open('tpm.mean.1-4.txt').readlines()
for i in range(len(tpm)):
    tpm[i]=tpm[i].rstrip('\n').split('\t')
    tpm[i][0]=tpm[i][0].strip('"')

result=[]
for i in range(len(genes)):
    
    target=genes[i][0]    
    
    start=0
    end=len(tpm)-1
    find=False
    while start+1<end:
        mid=start+int((end-start)/2)
        if tpm[mid][0]<target:
            start=mid
        elif tpm[mid][0]>target:
            end=mid
        else:
            loc=mid
            find=True
            break
    if find == False:
        if tpm[start][0]==target:
            loc=start
        elif tpm[end][0]==target:
            loc=end
        else:
            print('unmatched gene '+target)
            continue
    for j in range(1,len(tpm[loc])):
        genes[i].append(tpm[loc][j])
    result.append(genes[i])    

out_name=genes_name.rstrip('txt')+'tpm.txt'
out=open(out_name,'w')
for i in range(len(result)):
    out.write(''.join(str(result[i][j])+'\t' for j in range(len(result[i]))).rstrip('\t')+'\n')
out.close()