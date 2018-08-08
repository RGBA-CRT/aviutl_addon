## comment_video2nama.py
### なにこれ
+ えるえる氏作　AviUtl用 [ニコ生コメントプラグイン用](http://ch.nicovideo.jp/chaban/blomaga/ar525419) コメントコンバータ
+ 上記プラグインはニコ動のコメントだとうまく動作しないのでニコ生風に変換する  
+ Python 3系用
 
### やってること
+ utf8からsjisに変換
+ ニコ動のXMLはコメントの書き込み順なので、ニコ生と同じくvpos順にソートする

### 使い方
+ comment_video2nama.py ニコ動コメント.xml aviutl用コメント.xml