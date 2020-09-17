import jieba
from gensim import corpora, models, similarities
from punctuation import removePunctuation  # removePunctuation用来去除文本的标点符号及停用词
# from memory_profiler import profile

class EmptyError(Exception):
    def __init__(self):
        print('Empty!')

class Similarity:
    @staticmethod
    # @profile
    def similarity(file, test):
        file = removePunctuation(file)      # 去除停用词
        test = removePunctuation(test)
        texts = list()
        texts.append(file)
        texts.append('')
        texts = [jieba.lcut(text) for text in texts]
        dictionary = corpora.Dictionary(texts)              # 基于文本集建立【词典】，并获得词典特征数
        num_features = len(dictionary.token2id)

        corpus = [dictionary.doc2bow(text) for text in texts]       # 基于词典，将【分词列表集】转换成【稀疏向量集】，称作【语料库】

        tfidf = models.TfidfModel(corpus)       # 用语料库来训练TF-IDF模型

        new_vec = dictionary.doc2bow(jieba.lcut(test))      # 把测试文档进行分词并转换为二元组的向量
        index = similarities.SparseMatrixSimilarity(tfidf[corpus], num_features)        # 计算稀疏矩阵相似度，建立一个索引
        sim = index[tfidf[new_vec]]     # 根据索引得到最终的相似度
        return sim[0]



if __name__ == '__main__':
 # txt1 = open(sys.argv[1], 'r', encoding='UTF-8')
 txt1 = open('orig.txt', 'r', encoding='UTF-8')
 file = txt1.read()
 # txt2 = open(sys.argv[2], 'r', encoding='UTF-8')
 txt2 = open('blank.txt', 'r', encoding='UTF-8')
 test = txt2.read()
 if test == '':
     raise EmptyError
 else:
    txt2.close()
    ans = Similarity()
    ans = ans.similarity(file, test)
    # ans_txt = open(sys.argv[3], 'w', encoding='UTF-8')
    sim = str('%.2f' % ans)
    print(sim )
    # ans_txt.write(sim)
    # ans_txt.close()
