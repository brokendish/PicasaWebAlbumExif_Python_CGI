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
import picasaDisp
import picasaAlbumList

#フォームからデータを取得
formG = cgi.FieldStorage()

#クッキーからデータを取得
cookie = Cookie.SimpleCookie()
cookie.load(os.environ.get('HTTP_COOKIE', ''))
try:
  ur = cookie["ur_save"].value
  pw = cookie["pw_save"].value
except:
  ur = "1"
  pw = "2"

print u"Content-type: text/html;charset=utf-8".encode('utf-8')

print cookie.output()
print
print

print """
<html xmlns='http://www.w3.org/1999/xhtml' lang='ja'>
<body bgcolor='#585858' text='#E6D2B1'></body>
<style type='text/css'>
td, th { border: 1px #857464 solid; }
table { border: 1px #555555 solid; }
.aa{ background-color: #39303A; }
.bb{ font-size: small;background-color: #39303A; }
.cc{ background-color: #262625; }
#t_left{float: left;}
#t_right{float: left;}
#t_Btm{}
a:link { color: #E6D2B1; }
a:visited { color: #000080; }
a:hover { color: #E57400; }
a:active { color: #E57400; }
</style>
<h2>Picasa WebAlbum Exif情報取得</h2>
<HR>
"""

#print cookie.output()

print """
<script type="text/javascript" src="lightbox/js/prototype.js"></script>
<script type="text/javascript" src="lightbox/js/scriptaculous.js?load=effects,builder"></script>
<script type="text/javascript" src="lightbox/js/lightbox.js"></script>
<link rel="stylesheet" href="lightbox/css/lightbox.css" type="text/css" media="screen" />

<script language="javascript" type="text/javascript">

   //リンク文字列取得
   function getStr(self)
   {
      //リンクの文字列を「id=set_str」にセットする
      document.getElementById("set_albumname").value=self.firstChild.data;
      return self.firstChild.data;
   }
   //リンククリックでSubmitする
   function execute()
   {
      document.form1.button1.click();
   }
</script>
"""


#リンク文字列（アルバム名）を取得してリンククリックでアルバム内の情報を取得する
print """
<form  name="form1" method="POST" action="./picasa.cgi">
<input type="hidden" name="albumnameG" id="set_albumname" />
<input type="submit" value="submit" name="button1" style="visibility:hidden"><p>
</form>
"""

#print ur
#print pw

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
if albumname != "":
   picasaDisp.PicasaDisp(ur,pw,albumname).runDisp()
print "</div>"

#print """
#<div id="t_Btm">
#<table>
# <tr><td>
#  Picasa WebAlbum Exif情報取得  By brokendish.org
# </td></tr>
#</table>
#</div>
#"""
print '</div>'
print'</html>'
