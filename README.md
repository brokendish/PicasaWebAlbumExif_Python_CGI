Picasaウエブアルバムから指定されたアルバム内の全写真の詳細情報（Exif）を取得して表示する。
表示する情報は
・camera
・メーカ(make)
・モデル(model)
・ISO
・絞り(fstop)
・露出(exposure)
・レンズ焦点距離(focallength)
・フラッシュ(flash)
・日時(time)

●配置方法
マルッとCGIが動作するディレクトリに配置する
起動ファイルは「picasa.html」

「gdata」「atom」は特にいじっていない
「lightbox」は「lightbox.css」、「lightbox.js」で表示位置の調整,JSファイル、スタイルの参照部分の調整を行なっている。

●動作環境
Webサーバ上でPythonが実行可能であること

●注意
接続情報はCookieに保存される。今の所この情報は暗号化されていない。
