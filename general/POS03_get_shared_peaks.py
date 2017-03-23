input1 = input('please specify peak file 1:\n')
input2 = input('please specify peak file 2:\n')
list1 = open(input1).readlines()
for i in range(len(list1)):
    list1[i] =list1[i].strip('\n').split('\t')
list2 = open(input2).readlines()
for i in range(len(list2)):
    list2[i] = list2[i].strip('\n').split('\t')
gap=input('gap of overlapping peaks (bp): ')
from operator import itemgetter
list1 = sorted(list1,key=itemgetter(1,2))
list2 = sorted(list2,key=itemgetter(1,2))  
list_OL = []
p = 0
for i in range(len(list1)):
    for j in range(p,len(list2)):
        if list1[i][1] == list2[j][1]:
            if abs(int(list1[i][2])-int(list2[j][2])) <= int(gap):
                D = int(list1[i][2])-int(list2[j][2])
                record = ''.join(list1[i][a]+'\t' for a in range(len(list1[i])))+''.join(list2[j][b]+'\t' for b in range(len(list2[j])))+str(D)
                list_OL.append(record)
                p = j
                break
print('# of shared peaks in peak file 1:')
print(len(list_OL))
out_OL = open(input1.strip('txt')+'x.'+input2.strip('txt')+''+gap+'.txt','w')
for i in range(len(list_OL)):
    print(list_OL[i],file=out_OL)
out_OL.close()
