#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import logging

logger = logging.getLogger(__name__)

def get_tft_anxiety_message():
    """
    TFT不安解消の手順を返す - Herokuでの実行を考慮
    """
    # マークダウンファイルのパスを取得
    current_dir = os.path.dirname(os.path.abspath(__file__))
    markdown_path = os.path.join(current_dir, '..', 'resources', 'tft_anxiety.md')
    
    try:
        # マークダウンファイルを読み込む
        with open(markdown_path, 'r', encoding='utf-8') as file:
            markdown_text = file.read()
            logger.info(f"Successfully read markdown file from {markdown_path}")
            return markdown_text
    except FileNotFoundError:
        logger.warning(f"Markdown file not found at {markdown_path}, using fallback text")
        return get_fallback_text()
    except Exception as e:
        logger.error(f"Error reading markdown file: {str(e)}")
        return get_fallback_text()

def get_fallback_text():
    """
    フォールバックテキストを返す
    """
    return """# TFT 不安解消手順

**＜1＞** 問題をひとつ思い浮かべます。

**＜2＞** まず**PR**を15回タッピングまたは**圧通領域（基本は左側のみ、両側でも可）**を15回ほどさすります。

**＜3＞** **眉頭➡︎目の下➡︎わきの下➡︎鎖骨下**の順に2本指で5回ずつタッピングします。

**＜4＞ 9g(ナイン・ジー)：** 
ガミュート(手の甲の治療ポイント)をずっとタッピングしながら、各5回くらいタップする間に 
1. 目を開けます 
2. 目を閉じます 
3. 目を開けて、顔はまっすぐのまま、視線を右下に 
4. 視線を左下に 
5. 目を回転させて 
6. 目を反対回りに回転させます 
7. ハミング（例えば、咲いた咲いた♪のメロディーを鼻歌） 
8. 1から5まで数えます 
9. 再びハミング（例えば、咲いた咲いた♪のメロディーを鼻歌） 

※目の不自由な方は、目を開けたり、視線を下に向けていると想像しながらでも行えます。

**＜5＞** **眉頭➡︎目の下➡︎わきの下➡︎鎖骨下**の順に2本指で5回ずつタップします。

**＜6＞** **アイ・ロール** 
効果を落ち着かせるため、ガミュート(手の甲の治療ポイント)をタップしながら、顔はまっすぐ前のまま、10秒くらいかけて視線だけを床から天井まで動かします。"""
