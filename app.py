#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import logging
from flask import Flask, request, jsonify
from dotenv import load_dotenv
import hmac
import hashlib
import time
from commands.stress_relief import get_stress_relief_message, get_mindful_moment
from commands.tft_anxiety import get_tft_anxiety_message

# 環境変数の読み込み
load_dotenv()

# Flaskアプリケーションの初期化
app = Flask(__name__)

# ロギング設定
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Slack署名シークレット
SLACK_SIGNING_SECRET = os.environ.get("SLACK_SIGNING_SECRET", "")

def verify_slack_request(request_data, timestamp, signature):
    """
    Slackからのリクエスト検証
    """
    if not SLACK_SIGNING_SECRET:
        logger.warning("SLACK_SIGNING_SECRET is not set, skipping verification")
        return True
        
    # リクエスト有効期限（5分）
    if abs(time.time() - int(timestamp)) > 60 * 5:
        return False
        
    # 署名の照合
    req = f"v0:{timestamp}:{request_data}"
    request_hash = 'v0=' + hmac.new(
        SLACK_SIGNING_SECRET.encode(),
        req.encode(),
        hashlib.sha256
    ).hexdigest()
    
    return hmac.compare_digest(request_hash, signature)

@app.route('/slack/tft-fear-care', methods=['POST'])
def tft_fear_care():
    """
    /tft-fear-care コマンドのエンドポイント
    """
    # リクエスト検証
    if not verify_slack_request(
        request.get_data().decode('utf-8'),
        request.headers.get('X-Slack-Request-Timestamp', '0'),
        request.headers.get('X-Slack-Signature', '')
    ):
        return jsonify({"error": "Invalid request"}), 403
    
    # ユーザー情報の取得
    user_id = request.form.get('user_id', '')
    user_name = request.form.get('user_name', '')
    
    # ストレス解消メッセージの取得
    message = get_stress_relief_message()
    
    logger.info(f"Sent stress relief message to user: {user_name}")
    
    # Slackへの応答
    return jsonify({
        "response_type": "ephemeral",  # ユーザーのみに表示
        "text": message
    })

@app.route('/slack/mindful-moment', methods=['POST'])
def mindful_moment():
    """
    /mindful-moment コマンドのエンドポイント
    """
    # リクエスト検証
    if not verify_slack_request(
        request.get_data().decode('utf-8'),
        request.headers.get('X-Slack-Request-Timestamp', '0'),
        request.headers.get('X-Slack-Signature', '')
    ):
        return jsonify({"error": "Invalid request"}), 403
    
    # マインドフルネスのプロンプトを取得
    message = get_mindful_moment()
    
    return jsonify({
        "response_type": "ephemeral",
        "text": message
    })

@app.route('/slack/tft-anxiety', methods=['POST'])
def tft_anxiety():
    """
    /tft-anxiety コマンドのエンドポイント - TFT不安解消法
    """
    # リクエスト検証（省略可能：開発中は検証をスキップ）
    
    # シンプルな応答を返す - Slackの基本要件に忠実に従う
    return jsonify({
        "response_type": "ephemeral",
        "text": "TFT不安解消の手順です：\n\n" + 
                "1️⃣ 問題をひとつ思い浮かべます\n\n" +
                "2️⃣ PRを15回タッピングまたは圧通領域を15回さすります\n\n" +
                "3️⃣ 眉頭→目の下→わきの下→鎖骨下の順に2本指で5回ずつタップ\n\n" +
                "4️⃣ 9g：ガミュートをタップしながら：\n" +
                "   ・目を開ける→閉じる→右下に視線→左下に視線\n" + 
                "   ・目を回す→反対回りに回す→ハミング→1〜5まで数える→ハミング\n\n" +
                "5️⃣ 再度、眉頭→目の下→わきの下→鎖骨下の順にタップ\n\n" +
                "6️⃣ アイロール：ガミュートをタップしながら視線を床から天井まで動かす"
    })

@app.route('/', methods=['GET'])
def health_check():
    """
    ヘルスチェック用エンドポイント
    """
    return jsonify({"status": "ok", "message": "Slack Slash Commands Service is running"})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
