## comment_video2nama.py
aviutlでニコニコ動画のコメントを読み込ませるプラグインの補助ツール
### なにこれ
+ えるえる氏作　AviUtl用 [ニコ生コメントプラグイン用](http://ch.nicovideo.jp/chaban/blomaga/ar525419) コメントコンバータ
+ 上記プラグインはニコ動のコメントだとうまく動作しないのでニコ生風に変換する
+ Python 3系用
 
### やってること
+ utf8からsjisに変換
+ ニコ動のXMLはコメントの書き込み順なので、ニコ生と同じくvpos順にソートする

### 使い方
1. 「ニコ生のコメントを読み込ませるプラグイン」をAviUtlにインストール
   + 「@ニコニココメント読込.obj」を plugins\script に配置
1. ニコニコ動画からコメントファイル(XML, UTF-8)をダウンロード
   + 適当なツールでダウンロードする。作者はnicocacheを使用
1. 変換を実行する
   + 	```python comment_video2nama.py sm8.xml sm8_for_aviutl.xml```
   + ファイル名は好きなものに適宜変更する
   + pythonをインストールしていないならPython3系をインストールする
1. AviUtlを起動し、「ニコ生のコメントを読み込ませるプラグイン」からsm8_for_aviutl.xmlを読み込む
