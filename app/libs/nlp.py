
import math

from app.libs import jieba
# from app.libs.kw import key_words
from app.libs.lcs import LCS
from app.libs.ld import LD

"""
最后按 “标准差*平均值 &lt; 筛选阈值” 的条件按相关度由高至低添加，并返回最终结果  问题集的排序

向一个问题集中添加子问题
如果该问题集中已经有该子问题则按概率随机决定添加
概率为，其中k为常熟，x为已有的重复问题个数
添加成功时该问题集中所有非预设问题的”年龄“ + 1  问题集中的
”年龄“》预设值时该问题会被从问题集中删除
"""
def nlp(question, questions, answers):

    word_qs = []
    participle_qs = []

    _qa = dict(zip(questions, answers))

    for i in range(len(questions)):
        word_qs.append(list(questions[i]))
        participle_qs.append(list(jieba.cut(questions[i], cut_all=False)))

    word_ql = list(question)
    participle_ql = list(jieba.cut(question, cut_all=False))

    ll = {}

    for i in range(len(word_qs)):
        qstr = strToList(word_qs[i])
        a = [getLDRel(participle_qs[i], participle_ql), getLDRel(word_qs[i], word_ql), getLCSRel(participle_qs[i], participle_ql), getLCSRel(word_qs[i], word_ql)]
        ll[qstr] = getAllRel(a)

    lsort = sorted(ll.items(), key=lambda ll:ll[1])[-1]

    return _qa[lsort[0]]

def getLCSRel(a, b):
    return sum((x*x for x in LCS(a, b))) / (len(a) * len(b))

def getLDRel(qs, ql):
    return pow(1 - LD(qs, ql) / max(len(qs), len(ql)), 2)

def getAllRel(a):
    return math.sqrt(sum((x*x for x in a)) / len(a))

# def getKWRel(qs, ql):
#     if key_words(qs, ql)[0] == 0 or key_words(qs, ql) == 0:
#         return 0
#     return key_words(qs, ql)[0] / key_words(qs, ql)[1]

def strToList(l):
    str = ""
    for i in range(len(l)):
        str += l[i]
    return str

