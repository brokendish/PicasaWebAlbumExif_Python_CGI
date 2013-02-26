#!/usr/bin/python
# -*- coding: utf-8 -*-

import gdata.photos.service
import gdata.media
import gdata.geo
import getpass
import sys
import datetime
import cgi
import os
import Cookie
import picasaAlbumList
import urllib



##クッキーからデータを取得
#cookie = Cookie.SimpleCookie()
#cookie.load(os.environ.get('HTTP_COOKIE', ''))
#try:
#  ur = cookie["ur_save"].value
#  pw = cookie["pw_save"].value
#except:
#  ur = "1"
#  pw = "2"

print u"Content-type: text/html;charset=utf-8".encode('utf-8')

#フォームからデータを取得
formG = cgi.FieldStorage()
email=formG.getvalue('emailG', '')
password=formG.getvalue('passwordG', '')

ur=email
pw=password

##---------------------------------------------------
## 古典的暗号を使う（パッと見でわからなければいいので）     
##---------------------------------------------------
##ROT13単換字式暗号（シーザー暗号）ー暗号ーユーザ名
ur13=ur.encode('utf8').encode('base64_codec').encode('rot_13')
#クエリ文字列用のエンコード
ur13=urllib.quote_plus(ur13)

#cookie["ur_save"]=ur13
##ROT13単換字式暗号（シーザー暗号）ー複合ーユーザ名
#ur=ur13.decode('rot_13').decode('base64_codec').decode('utf8')
##---------------------------------------------------
##ROT13単換字式暗号（シーザー暗号）ー暗号ーパスワード
pw13=pw.encode('utf8').encode('base64_codec').encode('rot_13')
#クエリ文字列用のエンコード
pw13=urllib.quote_plus(pw13)

#cookie["pw_save"]=pw13
##ROT13単換字式暗号（シーザー暗号）ー複合ーパスワード
#pw=pw13.decode('rot_13').decode('base64_codec').decode('utf8')
##---------------------------------------------------

print """
<html xmlns='http://www.w3.org/1999/xhtml' lang='ja'>
<body bgcolor='#EFECED' text='#5E584E'></body>
<style type='text/css'>
td, th { border: 1px #857464 solid; }
table { border: 1px #555555 solid; }
.aa{ background-color: #5A5954; color: #FFFFFF; }
.bb{ font-size: small;background-color: #B7B4AC; }
.cc{ background-color: #5A5954; color: #FFFFFF}
.ee{ border: 0px solid;background-color: #5A5954; color: #FFFFFF}
.ff{ border: 0px solid;background-color: #5A5954; color: #FFFFFF;font-size:250%}
.ss{ border: 0px solid;background-color: #5A5954; color: #FFFFFF;font-size:small}
#t_left{float: left;}
#t_right{float: left;}
#t_Btm{}
a:link { color: #4D4D4D; }
a:visited { color: #000080; }
a:hover { color: #E57400; }
a:active { color: #E57400; }
</style>
"""
print """
<div id="t_Btm">
<table>
 <tr class="ee">
   <td rowspan=2>
     <a href="./picasa.html"><img src="./brokendish_iCON_Kuro.jpg" width="80" height="80"/></a>
   </td>
       <td class="ff"  valign=bottom>
        Picasa WebAlbum Exif(写真情報取得)
       </td>
     <tr class="ee">
       <td  class="ss" align=right>
         <a href="http://brokendish.org">http://brokendish.org</a>
       </td>
     </tr>
 </tr>
</table>
</div>
<hr>
"""

#print cookie.output()
#print ur13
#print pw13

print """
<script type="text/javascript" src="lightbox/js/prototype.js"></script>
<script type="text/javascript" src="lightbox/js/scriptaculous.js?load=effects,builder"></script>
<script type="text/javascript" src="lightbox/js/lightbox.js"></script>
<link rel="stylesheet" href="lightbox/css/lightbox.css" type="text/css" media="screen" />

<script language="javascript" type="text/javascript">

  var xmlHttp;
  var selal;

  function loadText(alb){
    xmlHttp = new XMLHttpRequest();
    xmlHttp.onreadystatechange = checkStatus;
    xmlHttp.open("POST", "./picasaDisp.cgi", true);
    xmlHttp.setRequestHeader("Content-Type", "application/x-www-form-urlencoded;charset=UTF-8");
    xmlHttp.send("albumname=" + alb + "&email=%s&password=%s");
  }

  function checkStatus(){
    if (xmlHttp.readyState == 4 && xmlHttp.status == 200){
      document.getElementById("t_right").innerHTML = xmlHttp.responseText;
    }
  }


   //リンク文字列取得
   function getStr(self)
   {
      //リンクの文字列を「id=set_str」にセットする
      document.getElementById("set_albumname").value=self.firstChild.data;
      selal=self.firstChild.data;
   }
   //リンククリックでSubmitする
   function execute()
   {
      document.getElementById("t_right").innerHTML = selal + " Now! Loading.."
      loadText(selal)
   }
</script>
""" % (ur13,pw13)

print """
<input type="hidden" name="albumnameG" id="set_albumname" />
<input type="submit" value="submit" name="button1" style="visibility:hidden"><p>
</form>
"""

#アルバム名
albumname = formG.getvalue("albumnameG","")

print '<div>'
#左側に表示
print '<div id="t_left">'
#Listデータ生成
picasaAlbumList.PicasaAlbumListDisp(ur,pw).runDisp()
print "</div>"

#右側に表示
print '<div id="t_right">'
#表示データ生成
#XMLHttpRequestを使用して結果をinnerHTMLで表示
print "</div>"

#print """
#<div id="t_Btm">
#<table>
# <tr><td>
#adasdasdas
# </td></tr>
#</table>
#</div>
#"""

print'</html>'
