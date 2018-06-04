# from app.libs import jieba.analyse
# import jieba.analyse
# def key_words(qs, ql):
#     qs_theme = jieba.analyse.textrank(qs, topK=3, withWeight=True, allowPOS=('ns', 'n', 'vn', 'v'))
#     ql_theme = jieba.analyse.textrank(ql, topK=3, withWeight=True, allowPOS=('ns', 'n', 'vn', 'v'))
#     kwRel = 0
#     sum = 0
#     for i in ql_theme:
#         for j in qs_theme:
#             if i[0] == j[0]:
#                 kwRel += j[1]
#     for m in qs_theme:
#         sum += m[1]
#     return [kwRel, sum]