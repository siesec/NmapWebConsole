# NmapWebConsole

NmapWebConsoleは、Nmapを使用してポートスキャンを実行し、その結果をWebインターフェースで確認するためのツールです。このアプリケーションは、スキャンの進行状況をリアルタイムで表示し、各ポートの状態を詳細に示します。

## 主な機能

- 指定されたIPアドレスとポート範囲でのNmapスキャン
- スキャン進行状況のリアルタイム表示
- 各ポートの状態（open、closed、filtered、unfiltered、open|filtered、closed|filtered）の表示とカウント
- スキャン結果のダウンロード

## 必要条件

- Python 3.x
- Bottleフレームワーク
- Nmap
- GNU Parallel

## インストール

1. 必要なPythonパッケージをインストールします。

    ```bash
    pip install bottle
    ```

2. NmapとGNU Parallelをインストールします。

    ```bash
    sudo apt-get install nmap
    sudo apt-get install parallel
    ```

## 使い方

1. アプリケーションを起動します。

    ```bash
    python app.py
    ```

2. ブラウザで以下のURLにアクセスします。

    ```
    http://localhost:8080
    ```

3. フォームに必要な情報（IPアドレス、入力ファイル、結果ファイル、並列ジョブ数）を入力し、スクリプトを生成します。
- Ports Fileにはあらかじめ1000ポート毎に分割して用意しているファイル名を指定します。
- Output Fileには`output.log`を指定します。*修正予定

4. 「Run Script」ボタンをクリックしてスキャンを開始します。進行状況と結果はリアルタイムで表示されます。

## ファイル構成

- `app.py`: メインのアプリケーションスクリプト
- `templates/`: HTMLテンプレートファイル
  - `index.html`: メインの入力フォーム
  - `progress.html`: スキャンの進行状況と結果を表示
  - `result.html`: スクリプト生成後のダウンロードリンク
  - `output.html`: エラーや出力メッセージを表示
- `ports_file/`
  - `ports_ポートレンジ.txt`:ポートの範囲が記載されたテキストファイル
- `output.log`:xxxx
- `run_parallel.sh`:xxxx
- `tools`:xxxx

## 注意事項

- スキャン対象のネットワークやデバイスに対して十分な権限を持っていることを確認してください。
- 不正なスキャンは法律に違反する可能性があります。
- スキャンの並列ジョブ数を設定する際は、対象のシステムに過度な負荷をかけないよう注意してください。

---#   N m a p W e b C o n s o l e 
 
 
