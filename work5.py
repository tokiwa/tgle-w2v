from flask import *
import gensim
import numpy
import pprint

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False
word2vec_model = gensim.models.KeyedVectors.load_word2vec_format('model/entity_vector.model.bin', binary=True)
# FAIL # word2vec_model = gensim.models.Word2Vec.load('model/entity_vector.model.bin')


# @app.route('/')   ＃flask1.0
@app.get('/')       #flask2.0
def get_request():
#    word2vec_model = gensim.models.KeyedVectors.load_word2vec_format('model/entity_vector.model.bin', binary=True)

    s1 = request.args.get('k1', '')
    s2 = request.args.get('k2', '')

    if s1 in word2vec_model.wv:
        return (s1 + " OK")
    else:
        return (s1 + " unknown")

#    pprint.pprint(word2vec_model.wv["東京大学"])
#        print(s1 + "unknown")

    print(s1)
#    s1="東京大学"
#    s2="京都大学"
    similarity = word2vec_model.similarity(s1, s2)
    print(type(similarity))
    return jsonify({"value": float(similarity)}), 200

if __name__ == "__main__":
    app.run(debug=True)