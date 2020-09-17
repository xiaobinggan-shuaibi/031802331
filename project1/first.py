import jieba
from gensim import corpora,models,similarities
from collections import defaultdict   #用于创建一个空的字典，在后续统计词频可清理频率少的词语
#1、读取文档
d1=open('orig_0.8_del.txt',encoding='UTF-8').read()
#d2=open('orig_0.8_add.txt',encoding='UTF-8').read()
d2=" "
#2、对要计算的文档进行分词
data1=jieba.cut(d1)
data2=jieba.cut(d2)
#3、对分词完的数据进行整理为指定格式
data11=""
for i in data1:
    data11+=i+" "
data21=""
for i in data2:
    data21+=i+" "
documents=[data11,data21]
texts=[[word for word in document.split()] for document in documents]
#4、 计算词语的频率
frequency=defaultdict(int)
for text in texts:
    for word in text:
        frequency[word]+=1

texts=[[word for word in text if frequency[word]>100] for text in texts]

#6、通过语料库将文档的词语进行建立词典
dictionary=corpora.Dictionary(texts)
#7、加载要对比的文档
d3=open('orig.txt',encoding='UTF-8').read()
data3=jieba.cut(d3)
data31=""
for i in data3:
    data31+=i+" "
#8、将要对比的文档通过doc2bow转化为稀疏向量
new_xs=dictionary.doc2bow(data31.split())
#9、对语料库进一步处理，得到新语料库
corpus=[dictionary.doc2bow(text)for text in texts]
#10、将新语料库通过tf-idf model 进行处理，得到tfidf
tfidf=models.TfidfModel(corpus)
#11、通过token2id得到特征数
featurenum=len(dictionary.token2id.keys())
#12、稀疏矩阵相似度，从而建立索引
index=similarities.SparseMatrixSimilarity(tfidf[corpus],num_features=featurenum)
#13、得到最终相似结果
sim=index[tfidf[new_xs]]
print(sim)
'''
doc1 = open('orig.txt','r',encoding='UTF-8')
txt1 = doc1.read()
doc2 = open('orig_0.8_add.txt','r',encoding='UTF-8')
txt2 = doc2.read()
cos = CosineSimilarity()
result = cos.cos_similarity(txt1,txt2)
print(result)
'''