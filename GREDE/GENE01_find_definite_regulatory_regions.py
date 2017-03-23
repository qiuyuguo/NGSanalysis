def find_chr(string):
    if string=='chrX':
        chr_num=20
    elif string=='chrY':
        chr_num=21
    else:
        chr_num=string.strip('chr')
        chr_num=int(chr_num)
    return chr_num

def in_chr(ch,x,y,d):
    c=find_chr(ch)-1
    if x>=0 and y<=gt[c][1]:
        return [ch,x,y,d]
    elif x<0 and y<=gt[c][1]:
        return [ch,0,y,d]
    elif x>=0 and y>gt[c][1]:
        return [ch,x,gt[c][1],d]
    
gt=open('mm9.gt').readlines()
for i in range(len(gt)):
    gt[i]=gt[i].rstrip('\n').split('\t')
    gt[i][1]=int(gt[i][1])
ref=open('mm9.great3.0.txt').readlines()
for i in range(len(ref)):
    ref[i]=ref[i].rstrip('\n').split('\t')
    ref[i][2]=int(ref[i][2])

# define regulatory domain as extending 500 kb from TSS in both direction

basal=[]
for i in range(len(ref)):
    basal.append(in_chr(ref[i][1],ref[i][2]-500000,ref[i][2]+500000,ref[i][3]))

# output
out=open('mm9.GREAT3.0.def.regulatory_domains.txt','w')
for i in range(len(basal)):
    print(ref[i][0]+'\t'+''.join(str(basal[i][j])+'\t' for j in range(len(basal[i])))+ref[i][4],file=out)
out.close()
    
    
