from flask import *
import gensim

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False
word2vec_model = gensim.models.KeyedVectors.load_word2vec_format('model/entity_vector.model.bin', binary=True)

@app.route('/similarity')
def similarity():
    word1 = request.args.get('word1', '')
    word2 = request.args.get('word2', '')

    similarity = word2vec_model.similarity(word1, word2)
    return jsonify({"similarity": float(similarity)}), 200

@app.route('/openai')
def openai():
    import openai
    import numpy as np
    import time

    time.sleep(5)
    word1 = request.args.get('word1', '')
    word2 = request.args.get('word2', '')
    openai.api_key = ""

    resp = openai.Embedding.create( input = [word1, word2], engine = "text-similarity-ada-001")

    embedding_a = resp['data'][0]['embedding']
    embedding_b = resp['data'][1]['embedding']
    similarity = np.dot(embedding_a, embedding_b)

    return jsonify({"similarity": float(similarity)}), 200

@app.get('/mostsimilar')
def mostsimilar():
    word = request.args.get('word', '')

    mostsimilar = word2vec_model.most_similar(positive=word, topn=5)

    return jsonify({"mostsimilar": str(mostsimilar)}), 200

if __name__ == "__main__":
    app.run(debug=True)
