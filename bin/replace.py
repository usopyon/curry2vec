#!/usr/bin/python
# coding: UTF-8

import sys
import re

f = open(sys.argv[1])
line = f.readline().rstrip()

while line:

  dict = [
    r"\s\d+\s",
    r"\s[　]{1,10}\s",
    r"\s[ぁ-ん]\s",
    r"\s[ａ-ｚ]\s",
    r"\s[Ａ-Ｚ]\s",
    r"\s[a-z]\s",
    r"\s[A-Z]\s"
  ]
  for pattern in dict:
    p = re.compile(pattern)
    line = p.sub(' ',line)

  dict = [
    'で','の','は','と','が','お','のみ',
    '編集','出典','脚注','概要','エピソード','特徴','関連','記事','コンテンツ',
    '項目','自体','社長','登録','業務用','掲載',
    '店舗','商品','説明','詳細',
    'もちろん','という','これ','この',
    'タイムセール','個',
    '動画','リンク','掲示板','アップロード','svg',
    '目次','非表示','紹介','内容',
    'ヘルプ','投稿','様',
    '地区','株式会社','所在地','本社','郵便','〒','系列','出店','近辺',
    '発売','期間','代金','引換','配送','合計','パッケージ','セット',
    '開始','終了','週間','週刊','以上','以下','今日',
    '写真','画像',
    'by','or','id','cn','de',
    'c','ｃ',
    'cal','ｃａｌ',
    'kcal','ｋｃａｌ',
    'g','ｇ',
    'kg','ｋｇ'
    'cc','ｃｃ'
    '県','府','市'
  ]
  for word in dict:
    line = line.replace(" "+word+" "," ")

  dict = [
    '[',']',
    '［','］',
    '(',')',
    '（','）',
    '{','}',
    '「','」',
    '『','』',
    '【','】',
    '≪','≫',
    '＜','＞',
    '《','》',
    '“','”',
    '"',"'",
    '!','！',
    ':','：',
    '@','＠',
    '#','＃',
    '*','＊',
    '~','～',
    '?','？',
    '\\','￥','円',
    '。','、','・','…','-','+','/','|','×','／','_','^',
    '◎','●','○','■','☆','★','♬','◆','◇',
    '↑','↓','←','→',
    '⇒',
    '笑'
  ]
  for word in dict:
    line = line.replace(word,'')

  print line
  line = f.readline()
