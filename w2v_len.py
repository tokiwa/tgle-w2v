from flask import *
import gensim
#import numpy

# save_word2vec_format で保存したモデル
word2vec_model = gensim.models.KeyedVectors.load_word2vec_format('model/entity_vector.model.bin', binary=True) #東北大
#word2vec_model = gensim.models.KeyedVectors.load_word2vec_format('model/jawiki_20180420_300d.txt')
#word2vec_model = gensim.models.KeyedVectors.load_word2vec_format('model/skipgram-retrofitting.txt')  #朝日新聞

# save で保存したモデル
#word2vec_model = gensim.models.KeyedVectors.load('model/chive-1.2-mc90.kv')
#word2vec_model = gensim.models.KeyedVectors.load('model/chive-1.2-mc5.kv')

vocab = word2vec_model.wv.vocab
print(len(vocab))
print(type(vocab))
# j = 0
# for i in vocab:
#     print(i)
#     j = j + 1
#     if j >= 300:
#         break



