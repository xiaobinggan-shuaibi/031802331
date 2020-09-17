import unittest
from main import Similarity


class EmptyError(Exception):
    def __init__(self):
        print('Empty!')

file = open('orig.txt', 'r', encoding='utf-8').read()
test = dict()
test['orig_0.8_add.txt'] = open('orig_0.8_add.txt', 'r', encoding='utf-8').read()
test['orig_0.8_del.txt'] = open('orig_0.8_del.txt', 'r', encoding='utf-8').read()
test['orig_0.8_dis_1.txt'] = open('orig_0.8_dis_1.txt', 'r', encoding='utf-8').read()
test['orig_0.8_dis_3.txt'] = open('orig_0.8_dis_3.txt', 'r', encoding='utf-8').read()
test['orig_0.8_dis_7.txt'] = open('orig_0.8_dis_7.txt', 'r', encoding='utf-8').read()
test['orig_0.8_dis_10.txt'] = open('orig_0.8_dis_10.txt', 'r', encoding='utf-8').read()
test['orig_0.8_dis_15.txt'] = open('orig_0.8_dis_15.txt', 'r', encoding='utf-8').read()
test['orig_0.8_mix.txt'] = open('orig_0.8_mix.txt', 'r', encoding='utf-8').read()
test['orig_0.8_rep.txt'] = open('orig_0.8_rep.txt', 'r', encoding='utf-8').read()
test['blank.txt'] = open('blank.txt','r',encoding='utf-8').read()

class Testsim(unittest.TestCase):
    def test_cosine(self):
        cos = Similarity()
        print('开始测试相似度！')
        for key in test.keys():
            if test[key] != '':
                result = cos.similarity(file, test[key])
                print('测试样本为：%s，相似度为：%.2f' % (key, result))
            else:
                raise EmptyError


if __name__ == '__main__':
    unittest.main()