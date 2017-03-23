## 20170112 read normalized reads count file -----------------------------------------------------------

reads=read.table('bcat-ATAC-01+09.150.m.1kb.reads_01-09-02-10.feQN.annotated.txt')
x=as.matrix(reads[,4:7])
ATAC1 = x[,1:2]
ATAC2 = x[,3:4]
dist = as.vector(reads[,8])
DE01=reads[which(rowMeans(ATAC1)<1000 & rowMeans(ATAC1)>5 & rowMeans(ATAC1)/rowMeans(ATAC2)>2 & abs(dist)>500),]
write.table(DE01,file='DE01.bcat-ATAC-01+09.150.m.1kb.reads_01-09-02-10.feQN.annotated.ATAC1_5.ATAC1_ATAC2_1.5.distal.txt',sep='\t',col.names = F, row.names = F)

reads=read.table('bcat-ATAC-03+12.150.m.1kb.reads_03-12-04-11.feQN.annotated.txt')
x=as.matrix(reads[,4:7])
ATAC3 = x[,1:2]
ATAC4 = x[,3:4]
dist = as.vector(reads[,8])
DE03=reads[which(rowMeans(ATAC3)<1000 & rowMeans(ATAC3)>5 & rowMeans(ATAC3)/rowMeans(ATAC4)>2 & abs(dist)>500),]
write.table(DE03,file='DE03.bcat-ATAC-03+12.150.m.1kb.reads_03-12-04-11.feQN.annotated.ATAC3_5.ATAC3_ATAC4_1.5.distal.txt',sep='\t',col.names = F, row.names = F)

reads=read.table('bcat-ATAC-04+11.150.m.1kb.reads_03-12-04-11.feQN.annotated.txt')
x=as.matrix(reads[,4:7])
ATAC3 = x[,1:2]
ATAC4 = x[,3:4]
dist = as.vector(reads[,8])
DE04=reads[which(rowMeans(ATAC4)<1000 & rowMeans(ATAC4)>5 & rowMeans(ATAC4)/rowMeans(ATAC3)>2 & abs(dist)>500),]
write.table(DE04,file='DE04.bcat-ATAC-04+11.150.m.1kb.reads_03-12-04-11.feQN.annotated.ATAC4_5.ATAC4_ATAC3_1.5.distal.txt',sep='\t',col.names = F, row.names = F)

## 20160112 find differentially opened reagions  -------------------------------------------------------

par(pin=c(3,3))
plot(log(ATAC1[,2]+0.1,10)~log(ATAC1[,1]+0.1,10),cex=0.1)

DE02=ATAC[which(ATAC3>5 & ATAC3/ATAC1>2 & abs(dist)>500),]
write.table(DE02,file='DE02.ATAC-all_10.150.merged.1kb.bcat-ATAC01-04.2kb.bcat-K27ac01-04.feQN.centered.annotated.ATAC3_5.ATAC3_ATAC1_2.txt',sep='\t',col.names = F, row.names = F)
DE03=ATAC[which(ATAC3>5 & ATAC3/ATAC4>2 & abs(dist)>500),]
write.table(DE03,file='DE03.ATAC-all_10.150.merged.1kb.bcat-ATAC01-04.2kb.bcat-K27ac01-04.feQN.centered.annotated.ATAC3_5.ATAC3_ATAC4_2.txt',sep='\t',col.names = F, row.names = F)
DE04=ATAC[which(ATAC4>5 & ATAC4/ATAC3>2 & abs(dist)>500),]
write.table(DE04,file='DE04.ATAC-all_10.150.merged.1kb.bcat-ATAC01-04.2kb.bcat-K27ac01-04.feQN.centered.annotated.ATAC4_5.ATAC4_ATAC3_2.txt',sep='\t',col.names = F, row.names = F)
DE09=ATAC[which(ATAC4>5 & ATAC4/ATAC1>2 & abs(dist)>500),]
write.table(DE09,file='DE09.ATAC-all_10.150.merged.1kb.bcat-ATAC01-04.2kb.bcat-K27ac01-04.feQN.centered.annotated.ATAC4_5.ATAC4_ATAC1_2.txt',sep='\t',col.names = F, row.names = F)

# 20161207 active enhancer ----------------------------------------------------------
DE05 = ATAC[which(ATAC1>5 & ATAC1/ATAC2>2 & K27ac1>3 & abs(dist)>500),]
write.table(DE05,file='DE05.ATAC-all_10.150.merged.1kb.bcat-ATAC01-04.2kb.bcat-K27ac01-04.feQN.centered.annotated.ATAC1_5.ATAC1_ATAC2_2.K27ac1_3+.txt',sep='\t',col.names = F, row.names = F)
DE06 = ATAC[which(ATAC1>5 & ATAC1/ATAC2>2 & K27ac1<=3 & abs(dist)>500),]
write.table(DE06,file='DE06.ATAC-all_10.150.merged.1kb.bcat-ATAC01-04.2kb.bcat-K27ac01-04.feQN.centered.annotated.ATAC1_5.ATAC1_ATAC2_2.K27ac1_3-.txt',sep='\t',col.names = F, row.names = F)
DE07 = ATAC[which(ATAC1>5 & ATAC3>5 & K27ac1>3 & abs(dist)>500),]
write.table(DE07,file='DE07.ATAC-all_10.150.merged.1kb.bcat-ATAC01-04.2kb.bcat-K27ac01-04.feQN.centered.annotated.ATAC1_5.ATAC3_5.K27ac1_3+.txt',sep='\t',col.names = F, row.names = F)
DE08 = ATAC[which(ATAC1>5 & ATAC4>5 & K27ac4>3 & K27ac4/K27ac3>2 & abs(dist)>500),]
write.table(DE08,file='DE08.ATAC-all_10.150.merged.1kb.bcat-ATAC01-04.2kb.bcat-K27ac01-04.feQN.centered.annotated.ATAC1_5.ATAC4_5.K27ac4+3.K27ac4_K27ac_2.txt',sep='\t',col.names = F, row.names = F)

# NPC_0 vs cortex

pos=ATAC1
neg=

pos_index=c()
neg_index=c()
#pvalue=c()
foldchange=c()
for (i in 1:nrow(pos)){
  #p=t.test(pos[i,],mu=neg[i])$p.value
  #p=t.test(pos[i,],neg[i,])$p.value
  #fc=mean(pos[i,]+0.01)/mean(neg[i]+0.01)
  fc=mean(pos[i,]+0.01)/mean(neg[i,]+0.01)
  #pvalue=c(pvalue,p)
  foldchange=c(foldchange,fc)
  if (mean(pos[i,])>5 & fc>3){
    pos_index=c(pos_index,i)
  }
  if (mean(neg[i,])>5 & fc<0.5){
    neg_index=c(neg_index,i)
  }
}
#all=cbind(rowMeans(pos),rowMeans(neg),foldchange,pvalue,pos,neg)
all=cbind(reads[,2],reads[,3],rowMeans(pos),rowMeans(neg),foldchange,pos,neg)
rownames(all) = reads[,1]
write.table(all,file='bcat_ATAC.norm.NPC_bcat_24_NPEM-vs-NPC_bcat_24_CHIR5.500bp.rc.all.txt',sep='\t',row.name=T,col.name=F)
pos_spec=all[pos_index,]
write.table(pos_spec,file='bcat_ATAC.norm.NPC_bcat_24_NPEM-vs-NPC_bcat_24_CHIR5.500bp.rc.pos.txt',sep='\t',row.name=T,col.name=F)
neg_spec=all[neg_index,]
write.table(neg_spec,file='bcat_ATAC.norm.NPC_bcat_24_NPEM-vs-NPC_bcat_24_CHIR5.500bp.rc.neg.txt',sep='\t',row.name=T,col.name=F)

## 20160909 hierarchical cluster

install.packages("gplots")
library("gplots")
install.packages("RColorBrewer")
library("RColorBrewer")

RowVar <- function(x) {
  rowSums((x - rowMeans(x))^2)/(dim(x)[2] - 1)
}

data=log(y[apply(y,1,max)>5,]+0.5,2)
data=data[apply(data,1,min)<log(25,2),]
TopVar=data[order(RowVar(data),decreasing=T),]
pdata=TopVar[1:5000,]

colnames(pdata)=c("bcat_NPC_0hr","bcat_cortex","bcat_NPC_24hr_NPEM","bcat_NPC_24hr_CHIR5",
                 "bcat_NPC_0hr","bcat_cortex","bcat_NPC_24hr_CHIR5","bcat_NPC_24hr_NPEM")

col_breaks = c(seq(-1,2.6,by=0.1),seq(2.7,3.4,by=0.1),seq(3.5,6.5,by=0.1))
my_palette <- colorRampPalette(c("white","red"))(n = length(col_breaks)-1)
#row_distance = dist(data, method = "euclidean")
#row_cluster = hclust(distance, method = "complete")    
#arguments for dist(): euclidean (default), maximum, canberra, binary, minkowski, manhattan
col_distance = dist(t(pdata), method = "euclidean")
#arguments for hclust(): complete (default), single, average, mcquitty, median, centroid, ward.D
col_cluster = hclust(col_distance, method = "complete")
pdf('hclust.bcat-ATAC-all.500bp.rc.fe.trim.sig_norm_5.topVar-5000.pdf')
heatmap.2(pdata,
          margins =c(12,9),     # widens margins around plot
          col=my_palette,       # use on color palette defined earlier 
          breaks=col_breaks,    # enable color transition at specified limits
          dendrogram="both",     # only draw a row dendrogram
          labRow=NA,
          key=T, keysize=1.5,
          trace="none",
          #Rowv = as.dendrogram(row_cluster), # apply default clustering method
          Colv = as.dendrogram(col_cluster)) # apply default clustering method)
dev.off()

## plot motif distribution

file = read.table('DE03.bcat-ATAC-03+12.150.m.1kb.reads_03-12-04-11.feQN.annotated.ATAC3_5.ATAC3_ATAC4_1.5.distal.200bp.motif1.2e-4.motif.txt')

mean(file$V3)-100
sd(file$V3)

pdf('DE03.bcat-ATAC-03+12.150.m.1kb.reads_03-12-04-11.feQN.annotated.ATAC3_5.ATAC3_ATAC4_1.5.distal.200bp.motif1.5e-4.motif.dist.pdf')
par(pin=c(3,3))
hist(file$V3,breaks=50,freq=TRUE,xaxt='n',xlab='',ylab='',main='')
z = c(0,50,100,150,200,250,300)
axis(1,at=z,label=c('-150','-100','-50','0','50','100','150'))
dev.off()

pdf('fimo.mm9_Osr1-BF_201205_vsFLAG_10.ctrl_10.ef_5.300bp.Wt1_motif.2e-5.motif.density.pdf')
hist(file$V3,breaks=50,freq=FALSE,xaxt='n',xlab='',ylab='',main='')
lines(density(file$V3),col ='green',lwd=3)
dev.off()