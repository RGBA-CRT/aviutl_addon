# aviutilニコ生コメント読み込みスクリプト向け
#  ニコ動コメント -> ニコ生コメント変換ツール
# python3用
# Programmed by RGBA_CRT 2018

import sys
import codecs
import xml.etree.ElementTree as ET

# 引数を処理
args = sys.argv
if len(args)!=3:
    print("usage:",args[0],"input.xml output.xml")
    exit(1)

# コメントファイル読み込み
try:
    f = open(args[1], 'r', encoding='utf-8')    
    rawxml = f.read()
    f.close()
except OSError as e:
    print(e)
    exit(1)


# XMLとしてパース
print("Loading "+args[1]+"...")
root = ET.fromstring(rawxml)

# コメントだけ抽出したリストを作成
comment_list = []
for child in root:
    if child.tag != "chat":  continue  # コメント抽出
    if child.text == None :  continue  # ゴミ除去
    comment_list.append(
        {
            "vpos": int(child.attrib["vpos"]),  # vposはソートのためにintに変換
            "text": child.text,
            "attrib": child.attrib
        }
    )

# vposでソート
comment_list_sorted = sorted(comment_list, key=lambda x: x["vpos"])

# XML出力
print("Writing XML to "+args[2]+"...")
try:
    fout = open(args[2], "wb")
    fout.write(b"<?xml version='1.0' encoding='shift_jis'?>\r\n<packet>\r\n")
    for comment in comment_list_sorted:
        str_list = []
        str_list.append("<chat ")
        for key, value in comment["attrib"].items():
            str_list.append("{0}=\"{1}\" ".format(key, value))
        str_list.append(">")
        str_list.append(comment["text"])
        str_list.append("</chat>\r\n")
        comment_line = ''.join(str_list)
        fout.write(comment_line.encode("shift_jis", "ignore"))

    fout.write(b"</packet>")
    fout.close()
    print("Done.")

except OSError as e:
    print(e)
    exit(1)

exit(0)