from flask import *
import gensim
#import numpy

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False
# save_word2vec_format で保存したモデル
word2vec_model = gensim.models.KeyedVectors.load_word2vec_format('model/entity_vector.model.bin', binary=True) #東北大
#word2vec_model = gensim.models.KeyedVectors.load_word2vec_format('model/jawiki_20180420_300d.txt')
#word2vec_model = gensim.models.KeyedVectors.load_word2vec_format('model/skipgram-retrofitting.txt')  #朝日新聞

# save で保存したモデル
#word2vec_model = gensim.models.KeyedVectors.load('model/chive-1.2-mc90.kv')
#word2vec_model = gensim.models.KeyedVectors.load('model/chive-1.2-mc5.kv')

@app.get('/knownword')
def knownword():
# Check keyword id known in entity_vector

    word = request.args.get('word','')
# ord2vec_model.wv works by gensim 3.8 not 4.0
    if word in word2vec_model.wv:
        return jsonify({"knownword": True}),200
    else:
        return jsonify({"knownword": False}),400

@app.get('/similarity')
def similarity():
    word1 = request.args.get('word1', '')
    word2 = request.args.get('word2', '')

    similarity = word2vec_model.similarity(word1, word2)
    return jsonify({"similarity": float(similarity)}), 200

@app.get('/positive')
def positive():
    word1 = request.args.get('word1', '')
    word2 = request.args.get('word2', '')
    word3 = request.args.get('word3', '')
    word = [word1, word2, word3]

    wordpositive = word2vec_model.most_similar(positive=word, topn=3)

    return jsonify({"wordpositive": str(wordpositive)}), 200

@app.get('/mostsimilar')
def mostsimilar():
    word = request.args.get('word', '')

    mostsimilar = word2vec_model.most_similar(positive=word, topn=5)

    return jsonify({"mostsimilar": str(mostsimilar)}), 200

if __name__ == "__main__":
    app.run(debug=True)
