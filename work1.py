# coding: utf-8
from flask import Flask, jsonify, abort, request

app = Flask(__name__)

# テストデータ
users = [
    {"id": "U001", "name": "ユーザ太郎", "age": 27},
    {"id": "U002", "name": "ユーザ二郎", "age": 20},
    {"id": "U003", "name": "ユーザ三郎", "age": 10}
]


#######################################################################
@app.route('/user/<string:id>', methods=['GET'])
def findUser(id):
    """
    ユーザを１件取得する
    """
    result = [n for n in users if n["id"] == id]

    if len(result) >= 1:
        # ユーザ情報を返却
        return jsonify(result)
    else:
        # 存在しないユーザIDが指定された
        abort(404)


#######################################################################
@app.route('/user/', methods=['POST'])
def createUser():
    """
    ユーザを登録する
    """
    # ユーザを追加
    data = {
        "id": request.form["id"],
        "name": request.form["name"],
        "age": int(request.form["age"])
    }
    users.append(data)

    # 正常に登録できたので、HTTP status=204(NO CONTENT)を返す
    return '', 204


#######################################################################
@app.route('/user/', methods=['PUT'])
def updateUser():
    """
    ユーザを更新する
    """
    id = request.form["id"]
    lst = [val for val in users if val["id"] == id]

    if len(lst) >= 1:
        lst[0]["name"] = request.form["name"]
        lst[0]["age"] = int(request.form["age"])
    else:
        # 存在しないユーザIDが指定された場合
        abort(404)

    # 正常に更新できたので、HTTP status=204(NO CONTENT)を返す
    return '', 204


#######################################################################
@app.route('/user/<string:id>', methods=['DELETE'])
def deleteUser(id):
    """
    ユーザを削除する
    """
    lst = [i for i, val in enumerate(users) if val["id"] == id]
    for index in lst:
        del users[index]

    if len(lst) >= 1:
        # ユーザの削除を行った場合、HTTP status=204(NO CONTENT)を返す
        return '', 204
    else:
        # 存在しないユーザIDが指定された場合
        abort(404)


if __name__ == "__main__":
    app.run(debug=True)