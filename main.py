# import jieba
# from gensim import corpora, models, similarities
# from punctuation import removePunctuation  # removePunctuation用来去除文本的标点符号及停用词
import sys
from cosine import Similarity


def main():
    txt1 = open(sys.argv[1], 'r', encoding='UTF-8')
    file = txt1.read()
    txt2 = open(sys.argv[2], 'r', encoding='UTF-8')
    test = txt2.read()
    txt2.close()
    ans = Similarity()
    ans = ans.similarity(file, test)
    ans_txt = open(sys.argv[3], 'w', encoding='UTF-8')
    sim = str('%.2f' % ans)
    ans_txt.write(sim)
    ans_txt.close()
    print(sim)

if __name__ == '__main__':
    main()
