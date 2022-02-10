from flask import Flask, request
app = Flask(__name__)
@app.route('/')
def get_request():
    contents = request.args.get('value', '')
    return contents
if __name__ == "__main__":
    app.run(debug=True)