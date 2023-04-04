# TGLE SIMILARITY (W2V)

## 概要

二つのキーワードをRequestとして取得し、Word2Vecによりそのキーワード間のSimilarityを計算し、その結果をResponseとして返します。Similarityの計算のためにGensimライブラリを必要とするため実装はPythonとし、フレームワークとしてFlaskを用いています。

![TGLEシステム構成図](TGLE.jpg)

## モデル

tgle-mkgroupの設定により、次のいずれかのAPIを利用します。

- 日本語 Wikipedia エンティティベクトル

    w2v_api.py　と同一ディレクトリに modelというディレクトリを作成し、そこに次のURLで示したWebサイトから日本語 Wikipedia エンティティベクトルをダウンロード/展開して得られる entity_vector.model.bin を配置します。
    ```
    http://www.cl.ecei.tohoku.ac.jp/~m-suzuki/jawiki_vector/
    ```

- OpenAI text-similarity-ada-001

    openai.api_key = "" の""内に、OpenAIから取得したアクセスキーを設定します。

## Flask起動

次のコマンドで起動します。
mkgroupからは、ポート 5555　にてアクセスします。 
```
% sudo FLASK_APP=w2v_api.py flask run --debugger --reload --port 5555 --host 0.0.0.0
```