import os
os.chdir('/Users/qiuyuguo/Dropbox/work/01_project_mouse_Six2/bioinformatics')

def binary_searh(target,great):
    start=0
    end=len(great)-1
    find=False
    while start+1<end:
        mid=start+int((end-start)/2)
        if great[mid][0]<target:
            start=mid
        elif great[mid][0]>target:
            end=mid
        else:
            loc=mid
            find=True
            break
    if find == False:
        if great[start][0]==target:
            loc=start
        elif great[end][0]==target:
            loc=end
        else:
            return([target,'NA',0])
    return great[loc][0:3]
    
tpm=open('tpm.E16.5Six2+_vs_E16.5Six2-.E16Cited1+_vs_P2Six2+.all.txt').readlines()
for i in range(len(tpm)):
    tpm[i]=tpm[i].rstrip('\n').split('\t')
    tpm[i][0]=tpm[i][0].strip('"')

#great1_name=input('genes list to be analyzed:\n')
great1_name='mm9_Six2-kid_201110_vsIgG_60.ctrl_10.ef_5.GREAT.hits.txt'
great1=open(great1_name).readlines()
for i in range(len(great1)):
    great1[i]=great1[i].rstrip('\n').split('\t')

#great2_name=input('genes list to be analyzed:\n')
great2_name='mm9_Hoxd11BF_201203_vsFLAG_30.ctrl_10.ef_5.GREAT.hits.txt'
great2=open(great2_name).readlines()
for i in range(len(great2)):
    great2[i]=great2[i].rstrip('\n').split('\t')
    
#great3_name=input('genes list to be analyzed:\n')
great3_name='mm9_Osr1-BF_201205_vsFLAG_10.ctrl_10.ef_5.GREAT.hits.txt'
great3=open(great3_name).readlines()
for i in range(len(great3)):
    great3[i]=great3[i].rstrip('\n').split('\t')
    
#great4_name=input('genes list to be analyzed:\n')
great4_name='mm9_Wt1-kid_20140823_vsInput_10.ctrl_10.ef_5.GREAT.hits.txt'
great4=open(great4_name).readlines()
for i in range(len(great4)):
    great4[i]=great4[i].rstrip('\n').split('\t')    

print('Attaching peak information...')            
result=[]
for i in range(len(tpm)):    
    target=tpm[i][0].strip('"')    
    add1=binary_searh(target,great1)
    add2=binary_searh(target,great2)
    add3=binary_searh(target,great3)
    add4=binary_searh(target,great4)
    rec=tpm[i]+add1+add2+add3+add4
    result.append(rec)    

out_name='tpm.E16.5Six2+_vs_E16.5Six2-.E16Cited1+_vs_P2Six2+.all.Six2_Hoxd11_Osr1_Wt1.GREAT.hits.txt'
out=open(out_name,'w')
for i in range(len(result)):
    out.write(''.join(str(result[i][j])+'\t' for j in range(len(result[i]))).rstrip('\t')+'\n')
out.close()