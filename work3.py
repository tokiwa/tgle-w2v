from flask import *
app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False

@app.route('/')
def get_request():
    contents = request.args.get('value', '')
    return jsonify({"value": contents}), 200
if __name__ == "__main__":
    app.run(debug=True)