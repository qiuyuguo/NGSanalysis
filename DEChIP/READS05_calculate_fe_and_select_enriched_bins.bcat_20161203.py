import os
import numpy as np
import pandas as pd

os.chdir('/Users/qiuyuguo/Dropbox/work/01_project_bcat/analysis/ChIP-Seq')

print('reading total reads count file...')
total_reads_count=open('FACS_mapped_reads_E16C+1_2_3_P2S+1_3.txt').readlines()
for i in range(len(total_reads_count)):
    total_reads_count[i]=total_reads_count[i].rstrip('\n').split('\t')
    total_reads_count[i][1]=float(total_reads_count[i][1])
#totalReads=pd.DataFrame([total_reads_count[i][1] for i in range(len(total_reads_count))])
readsFactor=np.diag([1/total_reads_count[i][1] for i in range(len(total_reads_count))])

print('reading read counts file...')
readsName='FACS_E16C+1_2_3_20150717.150.m.E16C+1_2_3_P2S+_1_3.txt'
readsFile=open(readsName).readlines()
for i in range(len(readsFile)):
    readsFile[i]=readsFile[i].rstrip('\n').rstrip('\t').split('\t')
    for j in range(1,len(readsFile[i])):
        readsFile[i][j]=float(readsFile[i][j])
colStart=[readsFile[i][0:3] for i in range(len(readsFile))]
for i in range(len(colStart)):
    colStart[i][1]=int(colStart[i][1])
    colStart[i][2]=int(colStart[i][2])

readsCount=np.array([readsFile[i][3:len(readsFile[i])] for i in range(len(readsFile))])

print('calculating region sizes...')
windowFactor=np.diag([1/(readsFile[i][2]-readsFile[i][1]) for i in range(len(readsFile))])

print('calculating fold enrichment...')
gs=2725765481
fe=np.dot(windowFactor,readsCount)
fe=np.dot(fe,readsFactor)
fe=fe*gs
fe=np.round(fe,2)

print('output fold enrichment file...')
feList=fe.tolist()
feFile=[]
for i in range(len(feList)):
    feFile.append(colStart[i]+feList[i])
feName=readsName.rstrip('txt')+'fe.txt'
outFe=open(feName,'w')
for i in range(len(feFile)):
    outFe.write(''.join(str(feFile[i][j])+'\t' for j in range(len(feFile[i]))).rstrip('\t')+'\n')
outFe.close()

print('quantile normalization')
[n,p]=fe.shape
print('get rank of data')
idx=np.argsort(fe,axis=0)
print('calculate reference signal intensity (average of all data sets)')
feSorted=np.sort(fe,axis=0)
feRef=np.mean(feSorted,axis=1)
print('apply reference signal intensity to ranked data')
feQN=fe
for j in range(p):
    feQN[idx[:,j],j]=feRef
feQN=np.round(feQN,2)

print('output fold enrichment file after quantile normalization...')
feQNList=feQN.tolist()
feQNFile=[]
for i in range(len(feQNList)):
    feQNFile.append(colStart[i]+feQNList[i])
feQNName=readsName.rstrip('txt')+'feQN.txt'
outFeQN=open(feQNName,'w')
for i in range(len(feQNFile)):
    outFeQN.write(''.join(str(feQNFile[i][j])+'\t' for j in range(len(feQNFile[i]))).rstrip('\t')+'\n')
outFeQN.close()
