# Slack スラッシュコマンド - ストレス解消

Slackのスラッシュコマンドを使用して、ストレス解消メッセージやマインドフルネスの練習を提供するPythonアプリケーションです。

## 機能

- `/tft-fear-care` - ストレス解消のためのメッセージをランダムに表示
- `/mindful-moment` - マインドフルネスの実践を促すプロンプトを表示
- `/tft-anxiety` - TFT（思考場療法）による不安解消の手順を表示

## 必要条件

- Python 3.8以上
- Slackワークスペースの管理者権限（アプリをインストールするため）
- Herokuアカウント（デプロイ用）

## ローカル開発環境のセットアップ

1. リポジトリをクローン

```bash
git clone https://github.com/yourusername/slack-slash-commands.git
cd slack-slash-commands
```

2. 仮想環境を作成して有効化

```bash
python -m venv venv
source venv/bin/activate  # Windowsの場合: venv\Scripts\activate
```

3. 依存パッケージをインストール

```bash
pip install -r requirements.txt
```

4. 環境変数の設定

```bash
cp .env.example .env
# .envファイルを編集して、実際の値を設定
```

5. アプリケーションの実行

```bash
flask run
# または
python app.py
```

## Slackアプリの設定

1. [Slack API](https://api.slack.com/apps) ページで新しいアプリを作成
2. 「Slash Commands」セクションで以下のコマンドを追加:
   - コマンド: `/tft-fear-care`
   - リクエストURL: `https://あなたのアプリのURL/slack/tft-fear-care`
   - 説明: 「ストレス解消のヒントを表示します」
   - 使用ヒント: `/tft-fear-care`
3. 同様に `/mindful-moment` コマンドも追加
4. 「OAuth & Permissions」で必要なスコープを追加:
   - `commands`
5. アプリをワークスペースにインストール

## Herokuへのデプロイ

1. Heroku CLIをインストール

2. Herokuにログインし、新しいアプリを作成

```bash
heroku login
heroku create your-app-name
```

3. 環境変数の設定

```bash
heroku config:set SLACK_SIGNING_SECRET=your_slack_signing_secret
```

4. デプロイ

```bash
git push heroku main
```

5. アプリの起動を確認

```bash
heroku open
```

6. Slackアプリの設定で、スラッシュコマンドのリクエストURLを更新:
   - `https://your-app-name.herokuapp.com/slack/tft-fear-care`
   - `https://your-app-name.herokuapp.com/slack/mindful-moment`

## カスタマイズ

`commands/stress_relief.py` ファイルを編集することで、表示されるメッセージをカスタマイズできます。また、新しいコマンドを追加する場合は、`app.py` に新しいルートを追加し、必要に応じて新しい機能を `commands/` ディレクトリに実装してください。

## セキュリティノート

本番環境では、Slackからのリクエスト検証を必ず有効にしてください。`SLACK_SIGNING_SECRET` 環境変数を設定することで、不正なリクエストを防止できます。

## ライセンス

MITライセンス
