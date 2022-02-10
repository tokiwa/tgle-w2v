from flask import *
import gensim
#import numpy

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False
word2vec_model = gensim.models.KeyedVectors.load_word2vec_format('model/entity_vector.model.bin', binary=True)

@app.route('/')
def get_request():
#    word2vec_model = gensim.models.KeyedVectors.load_word2vec_format('model/entity_vector.model.bin', binary=True)

    s1 = request.args.get('k1', '')
    s2 = request.args.get('k2', '')
    print(s1)
#    s1="東京大学"
#    s2="京都大学"
    similarity = word2vec_model.similarity(s1, s2)
    print(type(similarity))
    return jsonify({"value": float(similarity)}), 200

if __name__ == "__main__":
    app.run(debug=True)